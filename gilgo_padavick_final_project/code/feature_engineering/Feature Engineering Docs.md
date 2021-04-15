# Feature Engineering Docs

# Data Intuition - GUI Comparison

Taking a look at a few specific instances to compare data with Twitter GUI.

Looking at tweet 1372988670337245194:

id_str: 1372988670337245194

user.screen_name: EdgeCritical

entities.symbols: another dictionary that gives the ticker and indices within the tweet. In this example its: [{'text': 'gnus', 'indices': [75, 80]}]

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled.png)

He replied to himself? - Happens a lot due to Twitter character limit

in_reply_to_screen_name: EdgeCritical

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%201.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%201.png)

user.description: could be useful for categorizing users.

"Follow Me For Stock Related News & U..."

Now looking at tweet: 1372186152254472195

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%202.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%202.png)

Tweet number: 1372186031253037057

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%203.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%203.png)

Probably should include the rocket emoji as a feature: 

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%204.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%204.png)

Retweeted example:

Tweet ID: 1372689505312989189

![Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%205.png](Feature%20Engineering%20Docs%2070626c8d8ada4aef94c5908b85339d5b/Untitled%205.png)

# Important Features

```
created_at
entities.hashtags
entities.symbols
favorite_count
quoted_status.created_at
quoted_status.entities.hashtags
quoted_status.favorite_count
quoted_status.retweet_count
quoted_status.text
quoted_status.user.favourites_count
quoted_status.user.followers_count
quoted_status.user.friends_count
quoted_status.user.name
quoted_status.user.screen_name
quoted_status.user.verified
retweet_count
retweeted_status.created_at
retweeted_status.entities.hashtags
retweeted_status.favorite_count
retweeted_status.quoted_status.entities.hashtags
retweeted_status.quoted_status.entities.symbols
retweeted_status.quoted_status.favorite_count
retweeted_status.quoted_status.retweet_count
retweeted_status.quoted_status.text
retweeted_status.quoted_status.user.created_at
retweeted_status.quoted_status.user.favourites_count
retweeted_status.quoted_status.user.followers_count
retweeted_status.quoted_status.user.friends_count
retweeted_status.quoted_status.user.screen_name
retweeted_status.quoted_status.user.verified
retweeted_status.text
retweeted_status.user.created_at
retweeted_status.user.favourites_count	
retweeted_status.user.followers_count
retweeted_status.user.friends_count
retweeted_status.user.screen_name
retweeted_status.user.verified
stock
text
user.created_at
user.favourites_count
user.followers_count
user.friends_count
user.name
user.screen_name
user.verified
```

# Data Types

```
id                                                                          int64
id_str                                                                     object
text                                                                       object
truncated                                                                    bool
source                                                                     object
in_reply_to_status_id                                                     float64
in_reply_to_status_id_str                                                  object
in_reply_to_user_id                                                       float64
in_reply_to_user_id_str                                                    object
in_reply_to_screen_name                                                    object
geo                                                                        object
coordinates                                                                object
place                                                                      object
contributors                                                               object
is_quote_status                                                              bool
retweet_count                                                               int64
favorite_count                                                              int64
favorited                                                                    bool
retweeted                                                                    bool
possibly_sensitive                                                         object
lang                                                                       object
entities.hashtags                                                          object
entities.symbols                                                           object
entities.user_mentions                                                     object
entities.urls                                                              object
metadata.iso_language_code                                                 object
metadata.result_type                                                       object
user.id                                                                     int64
user.id_str                                                                object
user.name                                                                  object
user.screen_name                                                           object
user.location                                                              object
user.description                                                           object
user.url                                                                   object
user.entities.url.urls                                                     object
user.entities.description.urls                                             object
user.protected                                                               bool
user.followers_count                                                        int64
user.friends_count                                                          int64
user.listed_count                                                           int64
user.created_at                                                            object
user.favourites_count                                                       int64
user.utc_offset                                                            object
user.time_zone                                                             object
user.geo_enabled                                                             bool
user.verified                                                                bool
user.statuses_count                                                         int64
user.lang                                                                  object
user.contributors_enabled                                                    bool
user.is_translator                                                           bool
user.is_translation_enabled                                                  bool
user.profile_background_color                                              object
user.profile_background_image_url                                          object
user.profile_background_image_url_https                                    object
user.profile_background_tile                                                 bool
user.profile_image_url                                                     object
user.profile_image_url_https                                               object
user.profile_banner_url                                                    object
user.profile_link_color                                                    object
user.profile_sidebar_border_color                                          object
user.profile_sidebar_fill_color                                            object
user.profile_text_color                                                    object
user.profile_use_background_image                                            bool
user.has_extended_profile                                                    bool
user.default_profile                                                         bool
user.default_profile_image                                                   bool
user.following                                                             object
user.follow_request_sent                                                   object
user.notifications                                                         object
user.translator_type                                                       object
retweeted_status.created_at                                                object
retweeted_status.id                                                       float64
retweeted_status.id_str                                                    object
retweeted_status.text                                                      object
retweeted_status.truncated                                                 object
retweeted_status.entities.hashtags                                         object
retweeted_status.entities.symbols                                          object
retweeted_status.entities.user_mentions                                    object
retweeted_status.entities.urls                                             object
retweeted_status.metadata.iso_language_code                                object
retweeted_status.metadata.result_type                                      object
retweeted_status.source                                                    object
retweeted_status.in_reply_to_status_id                                    float64
retweeted_status.in_reply_to_status_id_str                                float64
retweeted_status.in_reply_to_user_id                                      float64
retweeted_status.in_reply_to_user_id_str                                  float64
retweeted_status.in_reply_to_screen_name                                  float64
retweeted_status.user.id                                                  float64
retweeted_status.user.id_str                                               object
retweeted_status.user.name                                                 object
retweeted_status.user.screen_name                                          object
retweeted_status.user.location                                             object
retweeted_status.user.description                                          object
retweeted_status.user.url                                                  object
retweeted_status.user.entities.url.urls                                    object
retweeted_status.user.entities.description.urls                            object
retweeted_status.user.protected                                            object
retweeted_status.user.followers_count                                     float64
retweeted_status.user.friends_count                                       float64
retweeted_status.user.listed_count                                        float64
retweeted_status.user.created_at                                           object
retweeted_status.user.favourites_count                                    float64
retweeted_status.user.utc_offset                                          float64
retweeted_status.user.time_zone                                           float64
retweeted_status.user.geo_enabled                                          object
retweeted_status.user.verified                                             object
retweeted_status.user.statuses_count                                      float64
retweeted_status.user.lang                                                float64
retweeted_status.user.contributors_enabled                                 object
retweeted_status.user.is_translator                                        object
retweeted_status.user.is_translation_enabled                               object
retweeted_status.user.profile_background_color                             object
retweeted_status.user.profile_background_image_url                         object
retweeted_status.user.profile_background_image_url_https                   object
retweeted_status.user.profile_background_tile                              object
retweeted_status.user.profile_image_url                                    object
retweeted_status.user.profile_image_url_https                              object
retweeted_status.user.profile_banner_url                                   object
retweeted_status.user.profile_link_color                                   object
retweeted_status.user.profile_sidebar_border_color                         object
retweeted_status.user.profile_sidebar_fill_color                           object
retweeted_status.user.profile_text_color                                   object
retweeted_status.user.profile_use_background_image                         object
retweeted_status.user.has_extended_profile                                 object
retweeted_status.user.default_profile                                      object
retweeted_status.user.default_profile_image                                object
retweeted_status.user.following                                           float64
retweeted_status.user.follow_request_sent                                 float64
retweeted_status.user.notifications                                       float64
retweeted_status.user.translator_type                                      object
retweeted_status.geo                                                      float64
retweeted_status.coordinates                                              float64
retweeted_status.place                                                    float64
retweeted_status.contributors                                             float64
retweeted_status.is_quote_status                                           object
retweeted_status.retweet_count                                            float64
retweeted_status.favorite_count                                           float64
retweeted_status.favorited                                                 object
retweeted_status.retweeted                                                 object
retweeted_status.possibly_sensitive                                        object
retweeted_status.lang                                                      object
quoted_status_id                                                          float64
quoted_status_id_str                                                       object
retweeted_status.quoted_status_id                                         float64
retweeted_status.quoted_status_id_str                                      object
retweeted_status.quoted_status.created_at                                  object
retweeted_status.quoted_status.id                                         float64
retweeted_status.quoted_status.id_str                                      object
retweeted_status.quoted_status.text                                        object
retweeted_status.quoted_status.truncated                                   object
retweeted_status.quoted_status.entities.hashtags                           object
retweeted_status.quoted_status.entities.symbols                            object
retweeted_status.quoted_status.entities.user_mentions                      object
retweeted_status.quoted_status.entities.urls                               object
retweeted_status.quoted_status.metadata.iso_language_code                  object
retweeted_status.quoted_status.metadata.result_type                        object
retweeted_status.quoted_status.source                                      object
retweeted_status.quoted_status.in_reply_to_status_id                      float64
retweeted_status.quoted_status.in_reply_to_status_id_str                  float64
retweeted_status.quoted_status.in_reply_to_user_id                        float64
retweeted_status.quoted_status.in_reply_to_user_id_str                    float64
retweeted_status.quoted_status.in_reply_to_screen_name                    float64
retweeted_status.quoted_status.user.id                                    float64
retweeted_status.quoted_status.user.id_str                                 object
retweeted_status.quoted_status.user.name                                   object
retweeted_status.quoted_status.user.screen_name                            object
retweeted_status.quoted_status.user.location                               object
retweeted_status.quoted_status.user.description                            object
retweeted_status.quoted_status.user.url                                   float64
retweeted_status.quoted_status.user.entities.description.urls              object
retweeted_status.quoted_status.user.protected                              object
retweeted_status.quoted_status.user.followers_count                       float64
retweeted_status.quoted_status.user.friends_count                         float64
retweeted_status.quoted_status.user.listed_count                          float64
retweeted_status.quoted_status.user.created_at                             object
retweeted_status.quoted_status.user.favourites_count                      float64
retweeted_status.quoted_status.user.utc_offset                            float64
retweeted_status.quoted_status.user.time_zone                             float64
retweeted_status.quoted_status.user.geo_enabled                            object
retweeted_status.quoted_status.user.verified                               object
retweeted_status.quoted_status.user.statuses_count                        float64
retweeted_status.quoted_status.user.lang                                  float64
retweeted_status.quoted_status.user.contributors_enabled                   object
retweeted_status.quoted_status.user.is_translator                          object
retweeted_status.quoted_status.user.is_translation_enabled                 object
retweeted_status.quoted_status.user.profile_background_color               object
retweeted_status.quoted_status.user.profile_background_image_url          float64
retweeted_status.quoted_status.user.profile_background_image_url_https    float64
retweeted_status.quoted_status.user.profile_background_tile                object
retweeted_status.quoted_status.user.profile_image_url                      object
retweeted_status.quoted_status.user.profile_image_url_https                object
retweeted_status.quoted_status.user.profile_banner_url                     object
retweeted_status.quoted_status.user.profile_link_color                     object
retweeted_status.quoted_status.user.profile_sidebar_border_color           object
retweeted_status.quoted_status.user.profile_sidebar_fill_color             object
retweeted_status.quoted_status.user.profile_text_color                     object
retweeted_status.quoted_status.user.profile_use_background_image           object
retweeted_status.quoted_status.user.has_extended_profile                   object
retweeted_status.quoted_status.user.default_profile                        object
retweeted_status.quoted_status.user.default_profile_image                  object
retweeted_status.quoted_status.user.following                             float64
retweeted_status.quoted_status.user.follow_request_sent                   float64
retweeted_status.quoted_status.user.notifications                         float64
retweeted_status.quoted_status.user.translator_type                        object
retweeted_status.quoted_status.geo                                        float64
retweeted_status.quoted_status.coordinates                                float64
retweeted_status.quoted_status.place                                      float64
retweeted_status.quoted_status.contributors                               float64
retweeted_status.quoted_status.is_quote_status                             object
retweeted_status.quoted_status.retweet_count                              float64
retweeted_status.quoted_status.favorite_count                             float64
retweeted_status.quoted_status.favorited                                   object
retweeted_status.quoted_status.retweeted                                   object
retweeted_status.quoted_status.possibly_sensitive                          object
retweeted_status.quoted_status.lang                                        object
quoted_status.created_at                                                   object
quoted_status.id                                                          float64
quoted_status.id_str                                                       object
quoted_status.text                                                         object
quoted_status.truncated                                                    object
quoted_status.entities.hashtags                                            object
quoted_status.entities.symbols                                             object
quoted_status.entities.user_mentions                                       object
quoted_status.entities.urls                                                object
quoted_status.entities.media                                               object
quoted_status.extended_entities.media                                      object
quoted_status.metadata.iso_language_code                                   object
quoted_status.metadata.result_type                                         object
quoted_status.source                                                       object
quoted_status.in_reply_to_status_id                                       float64
quoted_status.in_reply_to_status_id_str                                   float64
quoted_status.in_reply_to_user_id                                         float64
quoted_status.in_reply_to_user_id_str                                     float64
quoted_status.in_reply_to_screen_name                                     float64
quoted_status.user.id                                                     float64
quoted_status.user.id_str                                                  object
quoted_status.user.name                                                    object
quoted_status.user.screen_name                                             object
quoted_status.user.location                                                object
quoted_status.user.description                                             object
quoted_status.user.url                                                    float64
quoted_status.user.entities.description.urls                               object
quoted_status.user.protected                                               object
quoted_status.user.followers_count                                        float64
quoted_status.user.friends_count                                          float64
quoted_status.user.listed_count                                           float64
quoted_status.user.created_at                                              object
quoted_status.user.favourites_count                                       float64
quoted_status.user.utc_offset                                             float64
quoted_status.user.time_zone                                              float64
quoted_status.user.geo_enabled                                             object
quoted_status.user.verified                                                object
quoted_status.user.statuses_count                                         float64
quoted_status.user.lang                                                   float64
quoted_status.user.contributors_enabled                                    object
quoted_status.user.is_translator                                           object
quoted_status.user.is_translation_enabled                                  object
quoted_status.user.profile_background_color                                object
quoted_status.user.profile_background_image_url                            object
quoted_status.user.profile_background_image_url_https                      object
quoted_status.user.profile_background_tile                                 object
quoted_status.user.profile_image_url                                       object
quoted_status.user.profile_image_url_https                                 object
quoted_status.user.profile_banner_url                                      object
quoted_status.user.profile_link_color                                      object
quoted_status.user.profile_sidebar_border_color                            object
quoted_status.user.profile_sidebar_fill_color                              object
quoted_status.user.profile_text_color                                      object
quoted_status.user.profile_use_background_image                            object
quoted_status.user.has_extended_profile                                    object
quoted_status.user.default_profile                                         object
quoted_status.user.default_profile_image                                   object
quoted_status.user.following                                              float64
quoted_status.user.follow_request_sent                                    float64
quoted_status.user.notifications                                          float64
quoted_status.user.translator_type                                         object
quoted_status.geo                                                         float64
quoted_status.coordinates                                                 float64
quoted_status.place                                                       float64
quoted_status.contributors                                                float64
quoted_status.is_quote_status                                              object
quoted_status.retweet_count                                               float64
quoted_status.favorite_count                                              float64
quoted_status.favorited                                                    object
quoted_status.retweeted                                                    object
quoted_status.possibly_sensitive                                           object
quoted_status.lang                                                         object
entities.media                                                             object
extended_entities.media                                                    object
quoted_status.quoted_status_id                                            float64
quoted_status.quoted_status_id_str                                         object
retweeted_status.entities.media                                            object
retweeted_status.extended_entities.media                                   object
stock                                                                      object
```

Numeric columns

```
id                                                                          int64
truncated                                                                    bool
in_reply_to_status_id                                                     float64
in_reply_to_user_id                                                       float64
is_quote_status                                                              bool
retweet_count                                                               int64
favorite_count                                                              int64
favorited                                                                    bool
retweeted                                                                    bool
user.id                                                                     int64
user.protected                                                               bool
user.followers_count                                                        int64
user.friends_count                                                          int64
user.listed_count                                                           int64
user.favourites_count                                                       int64
user.geo_enabled                                                             bool
user.verified                                                                bool
user.statuses_count                                                         int64
user.contributors_enabled                                                    bool
user.is_translator                                                           bool
user.is_translation_enabled                                                  bool
user.profile_background_tile                                                 bool
user.profile_use_background_image                                            bool
user.has_extended_profile                                                    bool
user.default_profile                                                         bool
user.default_profile_image                                                   bool
retweeted_status.id                                                       float64
retweeted_status.in_reply_to_status_id                                    float64
retweeted_status.in_reply_to_status_id_str                                float64
retweeted_status.in_reply_to_user_id                                      float64
retweeted_status.in_reply_to_user_id_str                                  float64
retweeted_status.in_reply_to_screen_name                                  float64
retweeted_status.user.id                                                  float64
retweeted_status.user.followers_count                                     float64
retweeted_status.user.friends_count                                       float64
retweeted_status.user.listed_count                                        float64
retweeted_status.user.favourites_count                                    float64
retweeted_status.user.utc_offset                                          float64
retweeted_status.user.time_zone                                           float64
retweeted_status.user.statuses_count                                      float64
retweeted_status.user.lang                                                float64
retweeted_status.user.following                                           float64
retweeted_status.user.follow_request_sent                                 float64
retweeted_status.user.notifications                                       float64
retweeted_status.geo                                                      float64
retweeted_status.coordinates                                              float64
retweeted_status.place                                                    float64
retweeted_status.contributors                                             float64
retweeted_status.retweet_count                                            float64
retweeted_status.favorite_count                                           float64
quoted_status_id                                                          float64
retweeted_status.quoted_status_id                                         float64
retweeted_status.quoted_status.id                                         float64
retweeted_status.quoted_status.in_reply_to_status_id                      float64
retweeted_status.quoted_status.in_reply_to_status_id_str                  float64
retweeted_status.quoted_status.in_reply_to_user_id                        float64
retweeted_status.quoted_status.in_reply_to_user_id_str                    float64
retweeted_status.quoted_status.in_reply_to_screen_name                    float64
retweeted_status.quoted_status.user.id                                    float64
retweeted_status.quoted_status.user.url                                   float64
retweeted_status.quoted_status.user.followers_count                       float64
retweeted_status.quoted_status.user.friends_count                         float64
retweeted_status.quoted_status.user.listed_count                          float64
retweeted_status.quoted_status.user.favourites_count                      float64
retweeted_status.quoted_status.user.utc_offset                            float64
retweeted_status.quoted_status.user.time_zone                             float64
retweeted_status.quoted_status.user.statuses_count                        float64
retweeted_status.quoted_status.user.lang                                  float64
retweeted_status.quoted_status.user.profile_background_image_url          float64
retweeted_status.quoted_status.user.profile_background_image_url_https    float64
retweeted_status.quoted_status.user.following                             float64
retweeted_status.quoted_status.user.follow_request_sent                   float64
retweeted_status.quoted_status.user.notifications                         float64
retweeted_status.quoted_status.geo                                        float64
retweeted_status.quoted_status.coordinates                                float64
retweeted_status.quoted_status.place                                      float64
retweeted_status.quoted_status.contributors                               float64
retweeted_status.quoted_status.retweet_count                              float64
retweeted_status.quoted_status.favorite_count                             float64
quoted_status.id                                                          float64
quoted_status.in_reply_to_status_id                                       float64
quoted_status.in_reply_to_status_id_str                                   float64
quoted_status.in_reply_to_user_id                                         float64
quoted_status.in_reply_to_user_id_str                                     float64
quoted_status.in_reply_to_screen_name                                     float64
quoted_status.user.id                                                     float64
quoted_status.user.url                                                    float64
quoted_status.user.followers_count                                        float64
quoted_status.user.friends_count                                          float64
quoted_status.user.listed_count                                           float64
quoted_status.user.favourites_count                                       float64
quoted_status.user.utc_offset                                             float64
quoted_status.user.time_zone                                              float64
quoted_status.user.statuses_count                                         float64
quoted_status.user.lang                                                   float64
quoted_status.user.following                                              float64
quoted_status.user.follow_request_sent                                    float64
quoted_status.user.notifications                                          float64
quoted_status.geo                                                         float64
quoted_status.coordinates                                                 float64
quoted_status.place                                                       float64
quoted_status.contributors                                                float64
quoted_status.retweet_count                                               float64
quoted_status.favorite_count                                              float64
quoted_status.quoted_status_id                                            float64
```