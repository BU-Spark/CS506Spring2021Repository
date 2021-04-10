let files = [
  "ALL-StreetCleaning",
  "Cptry-BarrelStands",
  "Cptry-BoardUp",
  "Cptry-BuildingRepairs",
  "Cptry-CityFenceRepair",
  "Cptry-General",
  "Cptry-PublicStairs",
  "Cptry-Railings",
  "Cust-AmerLegionClean",
  "Cust-BathroomResupply",
  "Cust-BldgMaintenance",
  "Cust-Boiler-Heatcheck",
  "Cust-ChambersCheck",
  "Cust-CleanBathroom",
  "Cust-CleanDitch",
  "Cust-CleanElevator",
  "Cust-CleanMayor'sOfc",
  "Cust-Cleaning",
  "Cust-EquipmentMaintenance",
  "Cust-Events",
  "Cust-FurnitureMove-Removal",
  "Cust-Inmates-Roca",
  "Cust-MailDuty",
  "Cust-Mowing",
  "Cust-Newspapers",
  "Cust-OfficeRecycling",
  "Cust-OfficeTrash",
  "Cust-Open-CloseCityHall",
  "Cust-ResupplyOffices",
  "Cust-SoapDispensers",
  "Cust-WashFloor",
  "DR-CatchBasinClean",
  "DR-CatchBasinInspect",
  "DR-CatchBasinRebuild",
  "DR-Clvrt&TrashRackClean",
  "DR-ClvrtRepair",
  "DR-DrainPumpStation",
  "DR-InspctDrainContractor",
  "DR-LateralDrainClean",
  "DR-MarkOut-DigSafe",
  "DR-MissingGrate",
  "DR-MS4OutfallInspect",
  "DR-Other",
  "DR-StormCCTV",
  "DR-StormCulvertLocate",
  "DR-StormMainCleaning",
  "DR-StormManholeInspection",
  "DR-StormManholeLocate",
  "DR-StormOutfall",
  "DR-TideGateCleaning",
  "DR-TideGateMaintenance",
  "HYWY-ClearDebris-Pavement",
  "HYWY-CutAsphaltforExcavation",
  "HYWY-Mechanical",
  "HYWY-Other",
  "HYWY-PaintStreetMarkings",
  "HYWY-PavementRepair",
  "HYWY-Pothole",
  "HYWY-SandBarrels",
  "HYWY-Sidewalks",
  "HYWY-Trench",
  "Meters-BeachSampling",
  "Meters-CustomerComplaint",
  "Meters-DetectWaterLeak",
  "Meters-Disconnect(Seasonal)",
  "Meters-Freeze-Ups",
  "Meters-Install-SetMeter",
  "Meters-LowPressure",
  "Meters-MeterRead",
  "Meters-MeterRe-Read",
  "Meters-Other",
  "Meters-ServiceConnect",
  "Meters-ServiceDisconnect",
  "Meters-TurnOn-ShutOffs",
  "Meters-WaterSampling",
  "Parks-Bathrooms",
  "Parks-BuildingMaintenance",
  "Parks-CityParkMaintenance",
  "Parks-DogBagRefill",
  "Parks-Events",
  "Parks-Fields&Grounds",
  "Parks-GameSetup",
  "Parks-Graffiti",
  "Parks-Landscaping-Contractors",
  "Parks-Landscaping",
  "Parks-Lighting",
  "Parks-Mowing",
  "Parks-OpeningStadium",
  "Parks-Other",
  "Parks-Park-MemorialCleanup",
  "Parks-PlaygroundEquipment",
  "Parks-Spraying",
  "Parks-TrashCleanup",
  "Sanitation-BikeRemoval",
  "Sanitation-DeadAnimal",
  "Sanitation-Debris-LitterPickup",
  "Sanitation-DumpsterIssue",
  "Sanitation-GraffitiRemoval",
  "Sanitation-IllegalDumping",
  "Sanitation-Other",
  "Sanitation-Overgrowth",
  "Sanitation-PestControlOutdoor",
  "Sanitation-PublicBarrels",
  "Sanitation-PublicLandCleanup",
  "Sanitation-RecycleBarrel",
  "Sanitation-Spills",
  "Sanitation-StreetSweeping",
  "Sanitation-TrashCartDelivery",
  "Sanitation-TrashCartInspection",
  "Sanitation-TrashCartRemoval",
  "Sanitation-TrashCartRepair",
  "SEW-BackflowInspect",
  "SEW-FloodResponse",
  "SEW-InspctSewrContractor",
  "SEW-ManholeCleaning",
  "SEW-MarkOut-DigSafe",
  "SEW-Other",
  "SEW-PumpStationAlarm",
  "SEW-PumpStationInspct-Clean",
  "SEW-SewerBlockageMain",
  "SEW-SewerBlockagePrivate",
  "SEW-SewerCCTV",
  "SEW-SewerInvestigate",
  "SEW-SewerLineCleaning",
  "SEW-SewerManholeInspection",
  "SEW-SewerManholeLeak",
  "SEW-SewerManholeLocate",
  "SEW-SewerManholeOffsetRepair",
  "SEW-SSOResponse-Report",
  "Sig-Lights-Other",
  "Sig-Lights-SignalIssue",
  "Sig-Lights-SignalRepairs",
  "Sig-Lights-SignalTiming",
  "Sig-Lights-StreetLightMaintenance",
  "Sig-Lights-StreetLightRepairs",
  "Sig-Lights-WalkButton",
  "Signs-ChangeRequest",
  "Signs-CleanSign",
  "Signs-Memorials",
  "Signs-Newsigninstallation",
  "Signs-Other",
  "Signs-RemoveSign",
  "Signs-SignGraffiti",
  "Signs-SignRepair-Replace",
  "Snow-BlockedbyVehicle",
  "Snow-Blower",
  "Snow-Other",
  "Snow-ParkingLots",
  "Snow-PlowDamage",
  "Snow-Plowing",
  "Snow-SaltPublicBuilding",
  "Snow-SaltRoads",
  "Snow-Shoveling",
  "Snow-SpaceSaverPickup",
  "Trees-BranchDown",
  "Trees-Inspection",
  "Trees-StumpRemoval",
  "Trees-TreeDown",
  "Trees-TreeRemoval",
  "Trees-Trimming-Maintenance",
  "Water-Backflow-CrossConnectInspect",
  "Water-BoosterStation",
  "Water-ContractInspect",
  "Water-CurbStop",
  "Water-GateReplacement",
  "Water-HydrFlush",
  "Water-HydrInspect",
  "Water-HydrMaint",
  "Water-Leak",
  "Water-LeakDetection",
  "Water-LocateValve",
  "Water-LowPressure-Quality",
  "Water-MainBreak",
  "Water-MarkOut-DigSafe",
  "Water-Other",
  "Water-SinkHole",
  "Water-Turn-On-Shut-Offs",
  "Water-ValveExercise",
  "Water-ValveInspection",
  "Water-Waterboxrepair",
  "Water-WaterSampling",
  "Water-Waterwork",
  "WSD-EquipMaintenance",
];

let cats = new Set();
for (let file of files) {
  cats.add(file.split("-")[0]);
}

let wrapper = document.querySelector("#wrapper");
let categoryContainer = document.createElement("form");
categoryContainer.id = "categoryContainer";
wrapper.appendChild(categoryContainer);
// create the container for the subcategories
let radioContainer = document.createElement("form");
radioContainer.id = "radioContainer";
wrapper.appendChild(radioContainer);

for (let cat of cats) {
  let radio = document.createElement("input");
  let label = document.createElement("label");
  radio.type = "radio";
  radio.id = cat;
  radio.name = "cats";
  radio.value = cat;
  label.setAttribute("for", cat);
  label.innerHTML = cat;

  categoryContainer.appendChild(radio);
  categoryContainer.appendChild(label);
}

categoryContainer.addEventListener("change", function () {
  let catSelected = document.querySelector('input[name = "cats"]:checked')
    .value;

  let catFiles = files.filter((f) => f.split("-")[0] == catSelected);
  radioContainer.innerHTML = "";

  for (file of catFiles) {
    let radio = document.createElement("input");
    let label = document.createElement("label");
    radio.type = "radio";
    radio.id = file;
    radio.name = "files";
    radio.value = file;
    label.setAttribute("for", file);
    label.innerHTML = file;

    radioContainer.appendChild(radio);
    radioContainer.appendChild(label);
  }
  // auto-select the first radio
  radioContainer.children[0].click();
});

radioContainer.addEventListener("change", function () {
  let selected = document.querySelector('input[name = "files"]:checked').value;
  newPlot(selected);
});
// auto-select the first category
categoryContainer.children[0].click();
