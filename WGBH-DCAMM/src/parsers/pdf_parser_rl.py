# import tabula
# pdf_path = "/Users/richardlee/Downloads/WorkforceUtilizationSummaryReportApril2019.pdf"

# dfs = tabula.read_pdf(pdf_path, pages = 1)
# tabula.convert_into(pdf_path, "out_put.csv", output_format= "csv", pages='all')

import math
from operator import itemgetter
from typing import List
import sys
import pdfplumber
from PIL import ImageDraw, ImageFont, Image
from pdfplumber.table import TableFinder
from tqdm.asyncio import tqdm


def almost_equals(num1, num2, precision=5.0):
    return abs(num1 - num2) < precision


class Point:
    r = 4
    hr = r / 2
    tail = 5

    def __init__(self, *xy):
        if len(xy) == 1:
            xy = xy[0]
        self.x, self.y = xy
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)
        self.down = False
        self.up = False
        self.left = False
        self.right = False

    @property
    def symbol(self):
        direction_table = {
            (False, False, False, False): '◦',

            (True, False, False, False): '↑',
            (False, True, False, False): '↓',
            (True, True, False, False): '↕',

            (True, True, True, False): '⊢',
            (True, True, False, True): '⊣',

            (False, False, True, False): '→',
            (False, False, False, True): '←',
            (False, False, True, True): '↔',

            (True, False, True, True): '⊥',
            (False, True, True, True): '⊤',

            (True, True, True, True): '╋',

            (True, False, True, False): '┗',
            (True, False, False, True): '┛',

            (False, True, True, False): '┏',
            (False, True, False, True): '┛',

        }
        return direction_table[(self.up, self.down, self.right, self.left)]

    def __repr__(self):
        return "Point<X:{} Y:{}>".format(self.x, self.y)

    def distance(self, other: 'Point'):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

    @property
    def as_tuple(self):
        return self.x, self.y

    def draw(self, canvas: ImageDraw.ImageDraw, color='red'):
        canvas.ellipse((self.x - self.hr, self.y - self.hr, self.x + self.hr, self.y + self.hr), fill=color)
        if self.down:
            canvas.line(((self.x, self.y), (self.x, self.y + self.tail)), 'blue')
        if self.up:
            canvas.line(((self.x, self.y), (self.x, self.y - self.tail)), 'blue')
        if self.left:
            canvas.line(((self.x, self.y), (self.x - self.tail, self.y)), 'blue')
        if self.right:
            canvas.line(((self.x, self.y), (self.x + self.tail, self.y)), 'blue')

    def points_to_right(self, other_points: List['Point']):
        sorted_other_points = sorted(other_points, key=lambda other: other.x)
        filtered_other_points = filter(lambda o: almost_equals(o.y, self.y) and o != self and o.x > self.x,
                                       sorted_other_points)
        return list(filtered_other_points)

    def points_below(self, other_points: List['Point']):
        sorted_other_points = sorted(other_points, key=lambda other: other.y)
        filtered_other_points = filter(lambda o: almost_equals(o.x, self.x) and o != self and o.y > self.y,
                                       sorted_other_points)
        return list(filtered_other_points)

    def on_same_line(self, other: 'Point'):
        if self == other:
            return False
        if almost_equals(self.x, other.x) or almost_equals(self.y, other.y):
            return True
        return False

    def is_above(self, other: 'Point'):
        return self.y < other.y

    def is_to_right(self, other: 'Point'):
        return self.x > other.x

    def is_below(self, other: 'Point'):
        return self.y > other.y

    def is_to_left(self, other: 'Point'):
        return self.x < other.x

    def get_right(self, others: List['Point']):
        others = self.points_to_right(others)
        for point in others:
            if point.down:
                return point
        return None

    def get_bottom(self, others: List['Point'], left=False, right=False):
        others = self.points_below(others)
        for point in others:
            if point.up:
                if left:
                    if not point.right:
                        continue
                if right:
                    if not point.left:
                        continue
                return point
        return None

    def has_above(self, others: List['Point']):
        others = list(filter(lambda p: p.up, others))
        point = list(sorted(others, key=lambda p: p.y))[0]
        if point.is_above(self) and point.up:
            return True
        return False

    def copy(self, other: 'Point'):
        self.down = other.down
        self.up = other.up
        self.left = other.left
        self.right = other.right

    def merge(self, other: 'Point'):
        self.up |= other.up
        self.down |= other.down
        self.left |= other.left
        self.right |= other.right

    def __eq__(self, other: 'Point'):
        if not almost_equals(self.x, other.x):
            return False
        return almost_equals(self.y, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Line:

    def __init__(self, p1: 'Point', p2: 'Point'):
        self.p1 = p1
        self.p2 = p2
        self.vertical = almost_equals(self.x, self.cx)
        if self.vertical:
            if self.p1.is_above(self.p2):
                pass
            else:
                self.p1, self.p2 = self.p2, self.p1
        else:
            if self.p2.is_to_right(self.p1):
                pass
            else:
                self.p1, self.p2 = self.p2, self.p1

        if self.vertical:
            self.p1.down = True
            self.p2.up = True
        else:
            self.p1.right = True
            self.p2.left = True

    def __hash__(self):
        return hash((self.p1, self.p2, self.vertical))

    @property
    def x(self):
        return self.p1.x

    @property
    def y(self):
        return self.p1.y

    @property
    def cx(self):
        return self.p2.x

    @property
    def cy(self):
        return self.p2.y

    @property
    def length(self):
        return self.p1.distance(self.p2)

    def __repr__(self):
        return 'Line<p1:{} p2:{} {}>'.format(self.p1, self.p2, 'vertical' if self.vertical else 'horizontal')

    def draw(self, canvas: ImageDraw.ImageDraw, color='blue'):
        x, y = self.x, self.y
        cx, cy = self.cx, self.cy

        canvas.line(((x, y), (cx, cy)), color, width=2)

    @property
    def as_tuple(self):
        return (self.x, self.y), (self.cx, self.cy)

    def infite_intersect(self, other: 'Line'):
        line1 = self.as_tuple
        line2 = other.as_tuple
        x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])  # Typo was here

        def det(point_a, point_b):
            return point_a[0] * point_b[1] - point_a[1] * point_b[0]

        div = det(x_diff, y_diff)
        if div == 0:
            return None, None
        d = (det(*line1), det(*line2))
        x = det(d, x_diff) / div
        y = det(d, y_diff) / div
        return x, y

    def intersect(self, other: 'Line', print_fulness=False) -> bool:
        """ this returns the intersection of Line(pt1,pt2) and Line(ptA,ptB)
              returns a tuple: (xi, yi, valid, r, s), where
              (xi, yi) is the intersection
              r is the scalar multiple such that (xi,yi) = pt1 + r*(pt2-pt1)
              s is the scalar multiple such that (xi,yi) = pt1 + s*(ptB-ptA)
                  valid == 0 if there are 0 or inf. intersections (invalid)
                  valid == 1 if it has a unique intersection ON the segment    """
        point_1 = self.x, self.y
        point_2 = self.cx, self.cy
        point_a = other.x, other.y
        point_b = other.cx, other.cy
        if self.vertical:
            if self.y > self.cy:
                if self.y >= other.y >= self.cy:
                    pass
                else:
                    return False
        else:
            if other.y > other.cy:
                if other.y >= self.y >= other.cy:
                    pass
                else:
                    return False
        det_tolerance = 0.0001
        x1, y1 = point_1
        x2, y2 = point_2
        dx1 = x2 - x1
        dy1 = y2 - y1
        x, y = point_a
        xb, yb = point_b
        dx = xb - x
        dy = yb - y
        det = (-dx1 * dy + dy1 * dx)
        if math.fabs(det) < det_tolerance:
            return False
        det_inv = 1.0 / det
        r = det_inv * (-dy * (x - x1) + dx * (y - y1))
        s = det_inv * (-dy1 * (x - x1) + dx1 * (y - y1))
        if print_fulness:
            print('self segment', r)
            print('other segment', s)
        if r > 1 or s > 1:  # can't be higher than 1, 1 means they are NOT intersecting
            return False
        if r > -0.1 and s > -0.1:  # This can happen on edges, so we allow small inaccuracy
            return True
        return False

    def intersection(self, other: 'Line', print_fulness=False) -> (int, int):
        """ this returns the intersection of Line(pt1,pt2) and Line(ptA,ptB)
                      returns a tuple: (xi, yi, valid, r, s), where
                      (xi, yi) is the intersection
                      r is the scalar multiple such that (xi,yi) = pt1 + r*(pt2-pt1)
                      s is the scalar multiple such that (xi,yi) = pt1 + s*(ptB-ptA)
                          valid == 0 if there are 0 or inf. intersections (invalid)
                          valid == 1 if it has a unique intersection ON the segment    """
        point_1 = self.x, self.y
        point_2 = self.cx, self.cy
        point_a = other.x, other.y
        point_b = other.cx, other.cy
        det_tolerance = 1
        x1, y1 = point_1
        x2, y2 = point_2
        dx1 = x2 - x1
        dy1 = y2 - y1
        x, y = point_a
        xb, yb = point_b
        dx = xb - x
        dy = yb - y
        det = (-dx1 * dy + dy1 * dx)

        if math.fabs(det) < det_tolerance:
            return None, None
        det_inv = 1.0 / det
        r = det_inv * (-dy * (x - x1) + dx * (y - y1))
        s = det_inv * (-dy1 * (x - x1) + dx1 * (y - y1))
        xi = (x1 + r * dx1 + x + s * dx) / 2.0
        yi = (y1 + r * dy1 + y + s * dy) / 2.0
        if print_fulness:
            print('self segment', r)
            print('other segment', s)
        return (round(xi), round(yi)), round(r, 4), round(s, 4)

    def is_between(self, point: 'Point'):
        pt1 = self.p1
        pt2 = self.p2
        cross_product = (point.y - pt1.y) * (pt2.x - pt1.x) - (point.x - pt1.x) * (pt2.y - pt1.y)


        # compare versus epsilon for floating point values, or != 0 if using integers
        if abs(cross_product) > math.e:
            return False

        dot_product = (point.x - pt1.x) * (pt2.x - pt1.x) + (point.y - pt1.y) * (pt2.y - pt1.y)
        if dot_product < 0:
            return False

        squared_length_ba = (pt2.x - pt1.x) * (pt2.x - pt1.x) + (pt2.y - pt1.y) * (pt2.y - pt1.y)

        if dot_product > squared_length_ba:
            return False

        return True

    def on_line(self, point: 'Point'):
        if self.vertical:
            if almost_equals(self.p1.x, point.x):
                return True
        else:
            if almost_equals(self.p1.y, point.y):
                return True
        return False

    def __contains__(self, other: {'Line', 'Point'}):
        if type(other) == Line:
            if self.vertical == other.vertical:
                return False
            return self.intersect(other)
        if type(other) == Point:
            return self.is_between(other)
            pass

    def on_same_line(self, other: 'Line'):
        if other.vertical != self.vertical:
            return False
        if self.vertical:
            return self.x == other.x
        else:
            return self.y == other.y

    def __eq__(self, other: 'Line'):
        return self.on_same_line(other)

    def corner(self, other: 'Line'):
        if self.p1 == other.p1 or self.p2 == other.p2 or self.p1 == other.p2:
            return True
        return False

    def connected(self, other: 'Line'):
        return other.p1 in self or other.p2 in self

    def parallel(self, other: 'Line'):
        return self.vertical == other.vertical

    def on_corners(self, other: 'Point'):
        return other == self.p1 or other == self.p2

    def test_intersection(self, other: 'Line'):
        """ prints out a test for checking by hand... """
        print('Testing intersection of:')
        print('\t', self)
        print('\t', other)
        result = self.intersection(other, True)
        print("\t Intersection result =", Point(result[0]))
        print()


class Cell:
    """P1-------P2
        |       |
        |       |
        |       |
        |       |
       P4-------P3
    """
    try:
        font = ImageFont.truetype('arial', size=9)
    except:
        font = ImageFont.load_default()

    def __init__(self, p1, p2, p3, p4):
        self.p1: Point = p1
        self.p2: Point = p2
        self.p3: Point = p3
        self.p4: Point = p4
        self.text = ''
        self.words = []  # type: List[str]

    def __repr__(self):
        return 'Cell <"{}"> '.format(self.text.replace('\n', ' '))

    def get_text(self):
        return ''.join(map(itemgetter('text'),self.words))

    @property
    def clean_text(self) -> str:
        return self.text.replace('\n', ' ')

    def __hash__(self):
        return hash(self.text) + hash(self.as_tuple)

    def on_same_line(self, other: 'Cell'):
        return self.p1.on_same_line(other.p1)

    def on_same_row(self, other: 'Cell'):
        return self.p1.y == other.p1.y

    @property
    def as_tuple(self):
        return self.p1.as_tuple, self.p2.as_tuple, self.p3.as_tuple, self.p4.as_tuple

    def __eq__(self, other: 'Cell'):
        if self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3 and self.p4 == other.p4:
            return True
        if self.p1 == other.p2 and self.p2 == other.p3 and self.p3 == other.p4 and self.p4 == other.p1:
            return True
        if self.p1 == other.p3 and self.p2 == other.p4 and self.p3 == other.p1 and self.p4 == other.p2:
            return True
        if self.p1 == other.p4 and self.p2 == other.p1 and self.p3 == other.p2 and self.p4 == other.p3:
            return True

    @property
    def center(self):
        x = [p.x for p in [self.p1, self.p2, self.p3, self.p4]]
        y = [p.y for p in [self.p1, self.p2, self.p3, self.p4]]
        centroid = Point(sum(x) / 4, sum(y) / 4)
        return centroid

    def draw(self, canvas: ImageDraw.ImageDraw, color='black', width=1, text_color='black'):

        # canvas.rectangle((self.p1.as_tuple, self.p3.as_tuple), outline=color,)
        canvas.line((self.p1.as_tuple, self.p2.as_tuple), color, width)
        canvas.line((self.p2.as_tuple, self.p3.as_tuple), color, width)
        canvas.line((self.p3.as_tuple, self.p4.as_tuple), color, width)
        canvas.line((self.p4.as_tuple, self.p1.as_tuple), color, width)
        if self.text:
            canvas.text((self.p1.x + 3, self.p1.y + 3), self.text, fill=text_color, font=self.font)


    def print_cell(self):
        buffer = ''
        longest = max([len(word) for word in self.text.split("\n")])
        buffer += '┼' + "─" * longest + '┼\n'
        for text_line in self.text.split('\n'):
            buffer += "│" + text_line + ' ' * (longest - len(text_line))
            buffer += "│\n"
        buffer += '┼' + "─" * longest + '┼\n'
        print(buffer)

    def point_inside_polygon(self, point: 'Point', include_edges=True):
        """
        Test if point (x,y) is inside polygon poly.
        poly is N-vertices polygon defined as
        [(x1,y1),...,(xN,yN)] or [(x1,y1),...,(xN,yN),(x1,y1)]
        (function works fine in both cases)
        Geometrical idea: point is inside polygon if horizontal beam
        to the right from point crosses polygon even number of times.
        Works fine for non-convex polygons.
        """
        x, y = point.as_tuple
        x1, y1 = self.p1.as_tuple
        x2, y2 = self.p3.as_tuple
        return x1 < x < x2 and y1 < y < y2


class Table:

    def __init__(self, cells: List[Cell], skeleton: List[List[Cell]], ugly_table: List[List[str]], words, canvas=None):
        self.cells = cells
        self.canvas = canvas
        self.words = words
        self.skeleton = skeleton
        self.ugly_table = ugly_table
        self.global_map = {}

    def build_table(self):
        for y, (text_row, skeleton_row) in enumerate(zip(self.ugly_table, self.skeleton)):
            self.global_map[y] = {}
            for x, (text, cell) in enumerate(zip(text_row, skeleton_row)):
                for t_cell in self.cells:
                    if t_cell.point_inside_polygon(cell.center):
                        t_cell.text += text if text else ''
                        self.global_map[y][x] = t_cell

        processed_cells = []
        for cell in tqdm(self.cells, desc='Analyzing cells', unit='cells'):
            if cell in processed_cells:
                continue
            in_words = list(filter(lambda char: cell.point_inside_polygon(
                Point(char['x0'], char['top'])), self.words))
            cell.words = in_words
            processed_cells.append(cell)

        if self.canvas:
            for cell in self.cells:
                # print(cell.get_text())
                cell.draw(self.canvas)

    def get_col(self, col_id) -> List[Cell]:
        col = []
        for row in self.global_map.values():
            col.append(row[col_id])
        return col

    def get_row(self, row_id) -> List[Cell]:
        return list(self.global_map[row_id].values())

    def get_cell(self, x, y) -> Cell:
        return self.global_map[y][x]

    def get_cell_span(self, cell):
        temp = {}
        for row_id, row in self.global_map.items():

            for col_id, t_cell in row.items():
                if t_cell == cell:
                    if not temp.get(row_id, False):
                        temp[row_id] = {}
                    temp[row_id][col_id] = True
        row_span = len(temp)
        col_span = len(list(temp.values())[0])
        return row_span, col_span


class TableExtractor:

    def __init__(self, path):
        self.pdf = pdfplumber.open(path)
        self.draw = False
        self.debug = False

    @staticmethod
    def filter_lines(lines: List[Line]):
        new_lines = []
        lines = list(set(lines))
        la = new_lines.append
        for line1 in tqdm(lines, desc='Filtering lines', unit='lines'):
            if line1 in new_lines:
                continue
            la(line1)
        new_lines = list(set(new_lines))
        return new_lines

    @staticmethod
    def add_skeleton_points(points, line):
        points.append(line.p1)
        points.append(line.p2)

    def build_skeleton(self, lines):
        skeleton_points = []
        skeleton = []
        temp_point = Point(0, 0)
        temp_point.down = temp_point.up = temp_point.left = temp_point.right = True
        vertical = list(filter(lambda l: l.vertical, lines))
        horizontal = list(filter(lambda l: not l.vertical, lines))
        for line1 in tqdm(vertical, desc='Building table skeleton', unit='lines'):
            sys.stdout.flush()
            if line1.length < 3.0:
                continue
            self.add_skeleton_points(skeleton_points, line1)
            for line2 in horizontal:
                if line1 == line2:
                    continue
                self.add_skeleton_points(skeleton_points, line2)
                if line1.infite_intersect(line2):
                    p1 = Point(line1.infite_intersect(line2))
                    if p1 not in skeleton_points:
                        skeleton_points.append(p1)

                    for n, p in enumerate(skeleton_points):
                        skeleton_points[n].copy(temp_point)
                        if p == p1:
                            p1.copy(p)
                            skeleton_points[n] = p1
        skeleton_points = list(set(skeleton_points))
        sorted_y_points = sorted(skeleton_points, key=lambda other: other.y)
        for p1 in tqdm(sorted_y_points, desc='Building skeleton cells', unit='point'):
            p2 = p1.get_right(skeleton_points)
            if p2:
                p3 = p2.get_bottom(skeleton_points, right=True)
                p4 = p1.get_bottom(skeleton_points, left=True)
                if p3 and p4:
                    cell = Cell(p1, p2, p3, p4)
                    if cell not in skeleton:
                        skeleton.append(cell)
                    else:
                        continue
        return skeleton_points, skeleton

    @staticmethod
    def skeleton_to_2d_table(skeleton: List[Cell]) -> List[List[Cell]]:
        rows = []
        for cell in tqdm(skeleton, desc='Analyzing cell positions', unit='cells'):
            row = tuple(sorted(filter(lambda c: cell.on_same_row(c), skeleton), key=lambda c: c.p1.x))
            rows.append(row)
        rows = list(sorted(list(set(rows)), key=lambda c: c[0].p1.y))
        rows = [list(row) for row in rows]
        return rows

    def parse_page(self, page_n):
        if self.debug:
            print('Parsing page', page_n)
        page = self.pdf.pages[page_n]
        if self.debug:
            print('Rendering page')

        if self.debug:
            print('Finding tables')
        tables = TableFinder(page, {'snap_tolerance': 3, 'join_tolerance': 3})
        if self.debug:
            print('Found', len(tables.tables), 'tables')
        beaut_tables = []
        if self.draw:
            p_im = page.to_image(resolution=100)
            p_im.draw_lines(page.lines)
            p_im.save('page-{}-lines.png'.format(page_n + 1))
        if len(tables.tables) > 5:
            return []
        for n, table in enumerate(tables.tables):
            if self.draw:
                p_im.reset()
                im = Image.new('RGB', (page.width, page.height), (255,) * 3)
                canvas = ImageDraw.ImageDraw(im)
            ugly_table = table.extract()
            lines = []  # type: List[Line]
            cells = []  # type: List[Cell]
            for cell in tqdm(table.cells, desc='Parsing cells', unit='cells'):
                # p_im.draw_rect(cell)
                x1, y1, x2, y2 = cell
                p1 = Point(x1, y1)
                p1.right = True
                p1.down = True
                p2 = Point(x2, y1)
                p2.left = True
                p2.down = True
                p3 = Point(x2, y2)
                p3.up = True
                p3.left = True
                p4 = Point(x1, y2)
                p4.up = True
                p4.right = True
                line1 = Line(p1, p2)
                line2 = Line(p2, p3)
                line3 = Line(p3, p4)
                line4 = Line(p4, p1)
                lines.append(line1)
                lines.append(line2)
                lines.append(line3)
                lines.append(line4)
                cell = Cell(p1, p2, p3, p4)
                cells.append(cell)

            # for line in lines:
            #     p_im.draw_line(line.as_tuple)
            lines = self.filter_lines(lines)
            # for line in lines:
            #     line.draw(canvas, color='green')
            if self.draw:
                p_im.save('page-{}-{}_im.png'.format(page_n + 1, n))
                im.save('page-{}-{}.png'.format(page_n + 1, n))
            skeleton_points, skeleton = self.build_skeleton(lines.copy())
            if not skeleton_points:
                continue
            skeleton = self.skeleton_to_2d_table(skeleton)

            # for p in points:
            #     p.draw(canvas)

            beaut_table = Table(cells, skeleton, ugly_table, page.extract_words())
            beaut_table.build_table()
            if self.draw:
                for cell in beaut_table.cells:
                    cell.draw(canvas)
            if self.debug:
                print('Saving rendered table')
            if self.draw:
                p_im.save('page-{}-{}_im.png'.format(page_n + 1, n))
                im.save('page-{}-{}.png'.format(page_n + 1, n))
            if self.draw:
                canvas.rectangle((0,0,page.width,page.height),fill='white') #cleaning canvas
                for row_id, row in enumerate(skeleton):
                    for cell_id, cell in enumerate(row):
                        cell.text = '{}-{}'.format(row_id, cell_id)
                        cell.draw(canvas, color='green',text_color='red')
                im.save('page-{}-{}-skeleton.png'.format(page_n + 1, n))
            beaut_tables.append(beaut_table)

        return beaut_tables


# def pdfplumber_table_to_table():


if __name__ == '__main__':
    # datasheet = DataSheet(r"D:\PYTHON\py_pdf_stm\datasheets\stm32L\stm32L431\stm32L431_ds.pdf")
    # pdf_interpreter = PDFInterpreter(r"/mnt/d/PYTHON/py_pdf_stm/datasheets/stm32L/stm32L476/stm32L476_ds.pdf")
    # pdf_interpreter = TableExtractor(r"D:\PYTHON\py_pdf_stm\datasheets\stm32L\stm32L476\stm32L476_ds.pdf")
    # pdf_interpreter = PDFInterpreter(r"/mnt/d/PYTHON/py_pdf_stm/datasheets/KL/KL17P64M48SF6_ds.pdf")
    pdf_interpreter = TableExtractor(r"/Users/richardlee/Downloads/WorkforceUtilizationSummaryReportApril2019.pdf")
    # pdf_interpreter = PDFInterpreter(r"D:\PYTHON\py_pdf_stm\datasheets\KL\KL17P64M48SF6_ds.pdf")
    pdf_interpreter.draw = True
    pdf_interpreter.debug = True
    # pdf_interpreter = PDFInterpreter(pdf.table_root.childs[table])
    # print(pdf_interpreter.content)
    # tables = pdf_interpreter.parse_page(5)
    tables = pdf_interpreter.parse_page(16)
    print(tables)
    # pdf_interpreter.parse_page(1)
    # pdf_interpreter.save()
    # pdf_interpreter.table.print_table()
