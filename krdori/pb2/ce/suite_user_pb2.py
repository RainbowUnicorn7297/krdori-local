# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/suite_user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from krdori.pb2.ce import user_pb2 as krdori_dot_pb2_dot_ce_dot_user__pb2
from krdori.pb2.ce import user_character_pb2 as krdori_dot_pb2_dot_ce_dot_user__character__pb2
from krdori.pb2.ce import user_situation_pb2 as krdori_dot_pb2_dot_ce_dot_user__situation__pb2
from krdori.pb2.ce import user_deck_pb2 as krdori_dot_pb2_dot_ce_dot_user__deck__pb2
from krdori.pb2.ce import user_story_pb2 as krdori_dot_pb2_dot_ce_dot_user__story__pb2
from krdori.pb2.ce import user_practice_ticket_pb2 as krdori_dot_pb2_dot_ce_dot_user__practice__ticket__pb2
from krdori.pb2.ce import user_bonds_pb2 as krdori_dot_pb2_dot_ce_dot_user__bonds__pb2
from krdori.pb2.ce import user_band_rank_pb2 as krdori_dot_pb2_dot_ce_dot_user__band__rank__pb2
from krdori.pb2.ce import user_band_story_pb2 as krdori_dot_pb2_dot_ce_dot_user__band__story__pb2
from krdori.pb2.ce import user_item_pb2 as krdori_dot_pb2_dot_ce_dot_user__item__pb2
from krdori.pb2.ce import user_commons_live2d_pb2 as krdori_dot_pb2_dot_ce_dot_user__commons__live2d__pb2
from krdori.pb2.ce import user_episode_pb2 as krdori_dot_pb2_dot_ce_dot_user__episode__pb2
from krdori.pb2.ce import user_append_parameter_pb2 as krdori_dot_pb2_dot_ce_dot_user__append__parameter__pb2
from krdori.pb2.ce import user_music_inventory_pb2 as krdori_dot_pb2_dot_ce_dot_user__music__inventory__pb2
from krdori.pb2.ce import user_costume_pb2 as krdori_dot_pb2_dot_ce_dot_user__costume__pb2
from krdori.pb2.ce import user_after_live_talk_pb2 as krdori_dot_pb2_dot_ce_dot_user__after__live__talk__pb2
from krdori.pb2.ce import user_area_item_pb2 as krdori_dot_pb2_dot_ce_dot_user__area__item__pb2
from krdori.pb2.ce import user_resource_count_pb2 as krdori_dot_pb2_dot_ce_dot_user__resource__count__pb2
from krdori.pb2.ce import user_live_boost_pb2 as krdori_dot_pb2_dot_ce_dot_user__live__boost__pb2
from krdori.pb2.ce import user_exchanges_pb2 as krdori_dot_pb2_dot_ce_dot_user__exchanges__pb2
from krdori.pb2.ce import user_gacha_ticket_pb2 as krdori_dot_pb2_dot_ce_dot_user__gacha__ticket__pb2
from krdori.pb2.ce import user_gacha_status_pb2 as krdori_dot_pb2_dot_ce_dot_user__gacha__status__pb2
from krdori.pb2.ce import user_area_status_pb2 as krdori_dot_pb2_dot_ce_dot_user__area__status__pb2
from krdori.pb2.ce import user_login_bonus_pb2 as krdori_dot_pb2_dot_ce_dot_user__login__bonus__pb2
from krdori.pb2.ce import user_home_banner_pb2 as krdori_dot_pb2_dot_ce_dot_user__home__banner__pb2
from krdori.pb2.ce import user_stamp_pb2 as krdori_dot_pb2_dot_ce_dot_user__stamp__pb2
from krdori.pb2.ce import user_degree_pb2 as krdori_dot_pb2_dot_ce_dot_user__degree__pb2
from krdori.pb2.ce import user_bad_penalty_pb2 as krdori_dot_pb2_dot_ce_dot_user__bad__penalty__pb2
from krdori.pb2.ce import user_character_profile_live2d_pb2 as krdori_dot_pb2_dot_ce_dot_user__character__profile__live2d__pb2
from krdori.pb2.ce import user_event_exchanges_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__exchanges__pb2
from krdori.pb2.ce import user_event_item_list_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__item__list__pb2
from krdori.pb2.ce import user_purchase_pb2 as krdori_dot_pb2_dot_ce_dot_user__purchase__pb2
from krdori.pb2.ce import user_mission_pb2 as krdori_dot_pb2_dot_ce_dot_user__mission__pb2
from krdori.pb2.ce import user_generic_story_pb2 as krdori_dot_pb2_dot_ce_dot_user__generic__story__pb2
from krdori.pb2.ce import user_live_boost_recovery_item_pb2 as krdori_dot_pb2_dot_ce_dot_user__live__boost__recovery__item__pb2
from krdori.pb2.ce import user_high_score_rating_pb2 as krdori_dot_pb2_dot_ce_dot_user__high__score__rating__pb2
from krdori.pb2.ce import user_season_pb2 as krdori_dot_pb2_dot_ce_dot_user__season__pb2
from krdori.pb2.ce import user_qualify_tournament_music_score_pb2 as krdori_dot_pb2_dot_ce_dot_user__qualify__tournament__music__score__pb2
from krdori.pb2.ce import user_event_story_memorial_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__story__memorial__pb2
from krdori.pb2.ce import user_miracle_ticket_pb2 as krdori_dot_pb2_dot_ce_dot_user__miracle__ticket__pb2
from krdori.pb2.ce import user_miracle_ticket_exchanges_pb2 as krdori_dot_pb2_dot_ce_dot_user__miracle__ticket__exchanges__pb2
from krdori.pb2.ce import user_special_lottery_draw_result_pb2 as krdori_dot_pb2_dot_ce_dot_user__special__lottery__draw__result__pb2
from krdori.pb2.ce import user_music_score_pb2 as krdori_dot_pb2_dot_ce_dot_user__music__score__pb2
from krdori.pb2.ce import user_music_achievement_pb2 as krdori_dot_pb2_dot_ce_dot_user__music__achievement__pb2
from krdori.pb2.ce import user_birthday_story_pb2 as krdori_dot_pb2_dot_ce_dot_user__birthday__story__pb2
from krdori.pb2.ce import user_comment_banner_pb2 as krdori_dot_pb2_dot_ce_dot_user__comment__banner__pb2
from krdori.pb2.ce import user_title_pb2 as krdori_dot_pb2_dot_ce_dot_user__title__pb2
from krdori.pb2.ce import user_generic_animation_pb2 as krdori_dot_pb2_dot_ce_dot_user__generic__animation__pb2
from krdori.pb2.ce import user_music_shop_pb2 as krdori_dot_pb2_dot_ce_dot_user__music__shop__pb2
from krdori.pb2.ce import user_select_new_year_card_pb2 as krdori_dot_pb2_dot_ce_dot_user__select__new__year__card__pb2
from krdori.pb2.ce import user_gacha_count_ceiling_pb2 as krdori_dot_pb2_dot_ce_dot_user__gacha__count__ceiling__pb2
from krdori.pb2.ce import user_backstage_talk_set_pb2 as krdori_dot_pb2_dot_ce_dot_user__backstage__talk__set__pb2
from krdori.pb2.ce import user_new_music_introduction_pb2 as krdori_dot_pb2_dot_ce_dot_user__new__music__introduction__pb2
from krdori.pb2.ce import user_new_situation_introduction_pb2 as krdori_dot_pb2_dot_ce_dot_user__new__situation__introduction__pb2
from krdori.pb2.ce import user_friend_pb2 as krdori_dot_pb2_dot_ce_dot_user__friend__pb2
from krdori.pb2.ce import user_profile_situation_pb2 as krdori_dot_pb2_dot_ce_dot_user__profile__situation__pb2
from krdori.pb2.ce import user_profile_degree_pb2 as krdori_dot_pb2_dot_ce_dot_user__profile__degree__pb2
from krdori.pb2.ce import user_deco_frame_inventory_pb2 as krdori_dot_pb2_dot_ce_dot_user__deco__frame__inventory__pb2
from krdori.pb2.ce import user_deco_pins_inventory_pb2 as krdori_dot_pb2_dot_ce_dot_user__deco__pins__inventory__pb2
from krdori.pb2.ce import user_deco_equipment_pb2 as krdori_dot_pb2_dot_ce_dot_user__deco__equipment__pb2
from krdori.pb2.ce import user_music_video_inventory_pb2 as krdori_dot_pb2_dot_ce_dot_user__music__video__inventory__pb2
from krdori.pb2.ce import user_purchase_menu_last_visit_pb2 as krdori_dot_pb2_dot_ce_dot_user__purchase__menu__last__visit__pb2
from krdori.pb2.ce import user_skin_pb2 as krdori_dot_pb2_dot_ce_dot_user__skin__pb2
from krdori.pb2.ce import user_event_music_score_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__music__score__pb2
from krdori.pb2.ce import user_event_music_achievement_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__music__achievement__pb2
from krdori.pb2.ce import user_event_box_gacha_pb2 as krdori_dot_pb2_dot_ce_dot_user__event__box__gacha__pb2
from krdori.pb2.ce import user_monthly_purchase_pb2 as krdori_dot_pb2_dot_ce_dot_user__monthly__purchase__pb2
from krdori.pb2.ce import user_subscription_pb2 as krdori_dot_pb2_dot_ce_dot_user__subscription__pb2
from krdori.pb2.ce import user_matching_bonus_pb2 as krdori_dot_pb2_dot_ce_dot_user__matching__bonus__pb2
from krdori.pb2.ce import user_daily_live_pb2 as krdori_dot_pb2_dot_ce_dot_user__daily__live__pb2
from krdori.pb2.ce import user_daily_live_total_reward_history_pb2 as krdori_dot_pb2_dot_ce_dot_user__daily__live__total__reward__history__pb2
from krdori.pb2.ce import user_comeback_status_pb2 as krdori_dot_pb2_dot_ce_dot_user__comeback__status__pb2
from krdori.pb2.ce import user_graphical_information_pb2 as krdori_dot_pb2_dot_ce_dot_user__graphical__information__pb2
from krdori.pb2.ce import user_multi_live_count_reward_pb2 as krdori_dot_pb2_dot_ce_dot_user__multi__live__count__reward__pb2
from krdori.pb2.ce import user_digest_story_pb2 as krdori_dot_pb2_dot_ce_dot_user__digest__story__pb2
from krdori.pb2.ce import user_live_boost_use_bonus_limit_list_pb2 as krdori_dot_pb2_dot_ce_dot_user__live__boost__use__bonus__limit__list__pb2
from krdori.pb2.ce import user_receivable_present_location_list_pb2 as krdori_dot_pb2_dot_ce_dot_user__receivable__present__location__list__pb2
from krdori.pb2.ce import user_birthday_introduction_pb2 as krdori_dot_pb2_dot_ce_dot_user__birthday__introduction__pb2
from krdori.pb2.ce import user_team_live_festival_event_pb2 as krdori_dot_pb2_dot_ce_dot_user__team__live__festival__event__pb2
from krdori.pb2.ce import user_limited_exchanges_pb2 as krdori_dot_pb2_dot_ce_dot_user__limited__exchanges__pb2
from krdori.pb2.ce import user_add_music_difficulty_introduction_pb2 as krdori_dot_pb2_dot_ce_dot_user__add__music__difficulty__introduction__pb2
from krdori.pb2.ce import user_gallery_pb2 as krdori_dot_pb2_dot_ce_dot_user__gallery__pb2
from krdori.pb2.ce import user_deck_rating_pb2 as krdori_dot_pb2_dot_ce_dot_user__deck__rating__pb2
from krdori.pb2.ce import updated_band_deck_rank_pb2 as krdori_dot_pb2_dot_ce_dot_updated__band__deck__rank__pb2
from krdori.pb2.ce import user_stage_challenge_pb2 as krdori_dot_pb2_dot_ce_dot_user__stage__challenge__pb2
from krdori.pb2.ce import user_star_seal_pb2 as krdori_dot_pb2_dot_ce_dot_user__star__seal__pb2
from krdori.pb2.ce import user_auto_live_pb2 as krdori_dot_pb2_dot_ce_dot_user__auto__live__pb2
from krdori.pb2.ce import user_monthly_mission_pb2 as krdori_dot_pb2_dot_ce_dot_user__monthly__mission__pb2
from krdori.pb2.ce import user_monthly_mission_reward_pb2 as krdori_dot_pb2_dot_ce_dot_user__monthly__mission__reward__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ekrdori/pb2/ce/suite_user.proto\x12\rkrdori.pb2.ce\x1a\x18krdori/pb2/ce/user.proto\x1a\"krdori/pb2/ce/user_character.proto\x1a\"krdori/pb2/ce/user_situation.proto\x1a\x1dkrdori/pb2/ce/user_deck.proto\x1a\x1ekrdori/pb2/ce/user_story.proto\x1a(krdori/pb2/ce/user_practice_ticket.proto\x1a\x1ekrdori/pb2/ce/user_bonds.proto\x1a\"krdori/pb2/ce/user_band_rank.proto\x1a#krdori/pb2/ce/user_band_story.proto\x1a\x1dkrdori/pb2/ce/user_item.proto\x1a\'krdori/pb2/ce/user_commons_live2d.proto\x1a krdori/pb2/ce/user_episode.proto\x1a)krdori/pb2/ce/user_append_parameter.proto\x1a(krdori/pb2/ce/user_music_inventory.proto\x1a krdori/pb2/ce/user_costume.proto\x1a(krdori/pb2/ce/user_after_live_talk.proto\x1a\"krdori/pb2/ce/user_area_item.proto\x1a\'krdori/pb2/ce/user_resource_count.proto\x1a#krdori/pb2/ce/user_live_boost.proto\x1a\"krdori/pb2/ce/user_exchanges.proto\x1a%krdori/pb2/ce/user_gacha_ticket.proto\x1a%krdori/pb2/ce/user_gacha_status.proto\x1a$krdori/pb2/ce/user_area_status.proto\x1a$krdori/pb2/ce/user_login_bonus.proto\x1a$krdori/pb2/ce/user_home_banner.proto\x1a\x1ekrdori/pb2/ce/user_stamp.proto\x1a\x1fkrdori/pb2/ce/user_degree.proto\x1a$krdori/pb2/ce/user_bad_penalty.proto\x1a\x31krdori/pb2/ce/user_character_profile_live2d.proto\x1a(krdori/pb2/ce/user_event_exchanges.proto\x1a(krdori/pb2/ce/user_event_item_list.proto\x1a!krdori/pb2/ce/user_purchase.proto\x1a krdori/pb2/ce/user_mission.proto\x1a&krdori/pb2/ce/user_generic_story.proto\x1a\x31krdori/pb2/ce/user_live_boost_recovery_item.proto\x1a*krdori/pb2/ce/user_high_score_rating.proto\x1a\x1fkrdori/pb2/ce/user_season.proto\x1a\x37krdori/pb2/ce/user_qualify_tournament_music_score.proto\x1a-krdori/pb2/ce/user_event_story_memorial.proto\x1a\'krdori/pb2/ce/user_miracle_ticket.proto\x1a\x31krdori/pb2/ce/user_miracle_ticket_exchanges.proto\x1a\x34krdori/pb2/ce/user_special_lottery_draw_result.proto\x1a$krdori/pb2/ce/user_music_score.proto\x1a*krdori/pb2/ce/user_music_achievement.proto\x1a\'krdori/pb2/ce/user_birthday_story.proto\x1a\'krdori/pb2/ce/user_comment_banner.proto\x1a\x1ekrdori/pb2/ce/user_title.proto\x1a*krdori/pb2/ce/user_generic_animation.proto\x1a#krdori/pb2/ce/user_music_shop.proto\x1a-krdori/pb2/ce/user_select_new_year_card.proto\x1a,krdori/pb2/ce/user_gacha_count_ceiling.proto\x1a+krdori/pb2/ce/user_backstage_talk_set.proto\x1a/krdori/pb2/ce/user_new_music_introduction.proto\x1a\x33krdori/pb2/ce/user_new_situation_introduction.proto\x1a\x1fkrdori/pb2/ce/user_friend.proto\x1a*krdori/pb2/ce/user_profile_situation.proto\x1a\'krdori/pb2/ce/user_profile_degree.proto\x1a-krdori/pb2/ce/user_deco_frame_inventory.proto\x1a,krdori/pb2/ce/user_deco_pins_inventory.proto\x1a\'krdori/pb2/ce/user_deco_equipment.proto\x1a.krdori/pb2/ce/user_music_video_inventory.proto\x1a\x31krdori/pb2/ce/user_purchase_menu_last_visit.proto\x1a\x1dkrdori/pb2/ce/user_skin.proto\x1a*krdori/pb2/ce/user_event_music_score.proto\x1a\x30krdori/pb2/ce/user_event_music_achievement.proto\x1a(krdori/pb2/ce/user_event_box_gacha.proto\x1a)krdori/pb2/ce/user_monthly_purchase.proto\x1a%krdori/pb2/ce/user_subscription.proto\x1a\'krdori/pb2/ce/user_matching_bonus.proto\x1a#krdori/pb2/ce/user_daily_live.proto\x1a\x38krdori/pb2/ce/user_daily_live_total_reward_history.proto\x1a(krdori/pb2/ce/user_comeback_status.proto\x1a.krdori/pb2/ce/user_graphical_information.proto\x1a\x30krdori/pb2/ce/user_multi_live_count_reward.proto\x1a%krdori/pb2/ce/user_digest_story.proto\x1a\x38krdori/pb2/ce/user_live_boost_use_bonus_limit_list.proto\x1a\x39krdori/pb2/ce/user_receivable_present_location_list.proto\x1a.krdori/pb2/ce/user_birthday_introduction.proto\x1a\x31krdori/pb2/ce/user_team_live_festival_event.proto\x1a*krdori/pb2/ce/user_limited_exchanges.proto\x1a:krdori/pb2/ce/user_add_music_difficulty_introduction.proto\x1a krdori/pb2/ce/user_gallery.proto\x1a$krdori/pb2/ce/user_deck_rating.proto\x1a*krdori/pb2/ce/updated_band_deck_rank.proto\x1a(krdori/pb2/ce/user_stage_challenge.proto\x1a\"krdori/pb2/ce/user_star_seal.proto\x1a\"krdori/pb2/ce/user_auto_live.proto\x1a(krdori/pb2/ce/user_monthly_mission.proto\x1a/krdori/pb2/ce/user_monthly_mission_reward.proto\"\xb4?\n\x14SuiteUserGetResponse\x12,\n\x04user\x18\x01 \x01(\x0b\x32\x1e.krdori.pb2.ce.UserGetResponse\x12;\n\x12user_character_map\x18\x02 \x01(\x0b\x32\x1f.krdori.pb2.ce.UserCharacterMap\x12;\n\x12user_situation_map\x18\x03 \x01(\x0b\x32\x1f.krdori.pb2.ce.UserSituationMap\x12\x31\n\ruser_deck_map\x18\x04 \x01(\x0b\x32\x1a.krdori.pb2.ce.UserDeckMap\x12>\n\x14user_main_story_list\x18\x05 \x01(\x0b\x32 .krdori.pb2.ce.UserMainStoryList\x12H\n\x19user_practice_ticket_list\x18\x06 \x01(\x0b\x32%.krdori.pb2.ce.UserPracticeTicketList\x12\x35\n\x0fuser_bonds_list\x18\x07 \x01(\x0b\x32\x1c.krdori.pb2.ce.UserBondsList\x12:\n\x12user_band_rank_map\x18\x08 \x01(\x0b\x32\x1e.krdori.pb2.ce.UserBandRankMap\x12\x46\n\x1cuser_poppin_party_story_list\x18\t \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12\x43\n\x19user_afterglow_story_list\x18\n \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12I\n\x1fuser_pastel_palettes_story_list\x18\x0b \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12K\n!user_hello_happy_world_story_list\x18\x0c \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12\x41\n\x17user_roselia_story_list\x18\r \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12\x33\n\x0euser_item_list\x18\x0e \x01(\x0b\x32\x1b.krdori.pb2.ce.UserItemList\x12\x44\n\x17user_commons_live2d_map\x18\x0f \x01(\x0b\x32#.krdori.pb2.ce.UserCommonsLive2dMap\x12\x37\n\x10user_episode_map\x18\x10 \x01(\x0b\x32\x1d.krdori.pb2.ce.UserEpisodeMap\x12H\n\x19user_append_parameter_map\x18\x11 \x01(\x0b\x32%.krdori.pb2.ce.UserAppendParameterMap\x12H\n\x19user_music_inventory_list\x18\x12 \x01(\x0b\x32%.krdori.pb2.ce.UserMusicInventoryList\x12\x37\n\x10user_costume_map\x18\x13 \x01(\x0b\x32\x1d.krdori.pb2.ce.UserCostumeMap\x12N\n\x1duser_after_live_talk_list_map\x18\x15 \x01(\x0b\x32\'.krdori.pb2.ce.UserAfterLiveTalkListMap\x12:\n\x12user_area_item_map\x18\x16 \x01(\x0b\x32\x1e.krdori.pb2.ce.UserAreaItemMap\x12=\n\x13user_resource_count\x18\x17 \x01(\x0b\x32 .krdori.pb2.ce.UserResourceCount\x12\x35\n\x0fuser_live_boost\x18\x18 \x01(\x0b\x32\x1c.krdori.pb2.ce.UserLiveBoost\x12=\n\x13user_exchanges_list\x18\x19 \x01(\x0b\x32 .krdori.pb2.ce.UserExchangesList\x12\x42\n\x16user_gacha_ticket_list\x18\x1a \x01(\x0b\x32\".krdori.pb2.ce.UserGachaTicketList\x12@\n\x15user_gacha_status_map\x18\x1b \x01(\x0b\x32!.krdori.pb2.ce.UserGachaStatusMap\x12>\n\x14user_area_status_map\x18\x1d \x01(\x0b\x32 .krdori.pb2.ce.UserAreaStatusMap\x12>\n\x14user_login_bonus_map\x18\x1e \x01(\x0b\x32 .krdori.pb2.ce.UserLoginBonusMap\x12@\n\x15user_home_banner_list\x18  \x01(\x0b\x32!.krdori.pb2.ce.UserHomeBannerList\x12\x33\n\x0euser_stamp_map\x18! \x01(\x0b\x32\x1b.krdori.pb2.ce.UserStampMap\x12\x35\n\x0fuser_degree_map\x18\" \x01(\x0b\x32\x1c.krdori.pb2.ce.UserDegreeMap\x12\x37\n\x10user_bad_penalty\x18# \x01(\x0b\x32\x1d.krdori.pb2.ce.UserBadPenalty\x12W\n!user_character_profile_live2d_map\x18$ \x01(\x0b\x32,.krdori.pb2.ce.UserCharacterProfileLive2dMap\x12H\n\x19user_event_exchanges_list\x18% \x01(\x0b\x32%.krdori.pb2.ce.UserEventExchangesList\x12>\n\x14user_event_item_list\x18& \x01(\x0b\x32 .krdori.pb2.ce.UserEventItemList\x12\x39\n\x11user_purchase_map\x18\' \x01(\x0b\x32\x1e.krdori.pb2.ce.UserPurchaseMap\x12\x37\n\x10user_mission_map\x18( \x01(\x0b\x32\x1d.krdori.pb2.ce.UserMissionMap\x12\x42\n\x16user_generic_story_map\x18) \x01(\x0b\x32\".krdori.pb2.ce.UserGenericStoryMap\x12X\n\"user_live_boost_recovery_item_list\x18* \x01(\x0b\x32,.krdori.pb2.ce.UserLiveBoostRecoveryItemList\x12\x42\n\x16user_high_score_rating\x18+ \x01(\x0b\x32\".krdori.pb2.ce.UserHighScoreRating\x12T\n user_high_score_music_rating_map\x18, \x01(\x0b\x32*.krdori.pb2.ce.UserHighScoreMusicRatingMap\x12.\n\x0buser_season\x18- \x01(\x0b\x32\x19.krdori.pb2.ce.UserSeason\x12\x62\n\'user_qualify_tournament_music_score_map\x18. \x01(\x0b\x32\x31.krdori.pb2.ce.UserQualifyTournamentMusicScoreMap\x12O\n\x1duser_event_story_memorial_map\x18/ \x01(\x0b\x32(.krdori.pb2.ce.UserEventStoryMemorialMap\x12K\n\x1buser_released_bonds_id_list\x18\x30 \x01(\x0b\x32&.krdori.pb2.ce.UserReleasedBondsIdList\x12\x44\n\x17user_miracle_ticket_map\x18\x32 \x01(\x0b\x32#.krdori.pb2.ce.UserMiracleTicketMap\x12W\n!user_miracle_ticket_exchanges_map\x18\x33 \x01(\x0b\x32,.krdori.pb2.ce.UserMiracleTicketExchangesMap\x12K\n$user_multi_disconnection_bad_penalty\x18\x34 \x01(\x0b\x32\x1d.krdori.pb2.ce.UserBadPenalty\x12\\\n$user_special_lottery_draw_result_map\x18\x35 \x01(\x0b\x32..krdori.pb2.ce.UserSpecialLotteryDrawResultMap\x12>\n\x14user_music_score_map\x18\x36 \x01(\x0b\x32 .krdori.pb2.ce.UserMusicScoreMap\x12J\n\x1auser_music_achievement_map\x18\x37 \x01(\x0b\x32&.krdori.pb2.ce.UserMusicAchievementMap\x12\x44\n\x17user_birthday_story_map\x18\x38 \x01(\x0b\x32#.krdori.pb2.ce.UserBirthdayStoryMap\x12=\n\x13user_comment_banner\x18\x39 \x01(\x0b\x32 .krdori.pb2.ce.UserCommentBanner\x12,\n\nuser_title\x18: \x01(\x0b\x32\x18.krdori.pb2.ce.UserTitle\x12J\n\x1auser_generic_animation_map\x18; \x01(\x0b\x32&.krdori.pb2.ce.UserGenericAnimationMap\x12<\n\x13user_music_shop_map\x18\x41 \x01(\x0b\x32\x1f.krdori.pb2.ce.UserMusicShopMap\x12\x35\n\x0fuser_title_list\x18\x42 \x01(\x0b\x32\x1c.krdori.pb2.ce.UserTitleList\x12\x62\n\'user_purchase_void_bad_penalty_standard\x18\x43 \x01(\x0b\x32\x31.krdori.pb2.ce.UserPurchaseVoidBadPenaltyStandard\x12N\n\x1duser_select_new_year_card_map\x18\x44 \x01(\x0b\x32\'.krdori.pb2.ce.UserSelectNewYearCardMap\x12M\n\x1cuser_gacha_count_ceiling_map\x18\x45 \x01(\x0b\x32\'.krdori.pb2.ce.UserGachaCountCeilingMap\x12\x63\n(user_backstage_talk_set_read_history_map\x18\x46 \x01(\x0b\x32\x31.krdori.pb2.ce.UserBackstageTalkSetReadHistoryMap\x12S\n\x1fuser_new_music_introduction_map\x18G \x01(\x0b\x32*.krdori.pb2.ce.UserNewMusicIntroductionMap\x12[\n#user_new_situation_introduction_map\x18H \x01(\x0b\x32..krdori.pb2.ce.UserNewSituationIntroductionMap\x12L\n\x1buser_friend_relation_detail\x18I \x01(\x0b\x32\'.krdori.pb2.ce.UserFriendRelationDetail\x12w\n3user_not_have_view_exchanges_miracle_ticket_id_list\x18J \x01(\x0b\x32:.krdori.pb2.ce.UserNotHaveViewExchangesMiracleTicketIdList\x12\x43\n\x16user_profile_situation\x18K \x01(\x0b\x32#.krdori.pb2.ce.UserProfileSituation\x12\x44\n\x17user_profile_degree_map\x18L \x01(\x0b\x32#.krdori.pb2.ce.UserProfileDegreeMap\x12O\n\x1duser_deco_frame_inventory_map\x18M \x01(\x0b\x32(.krdori.pb2.ce.UserDecoFrameInventoryMap\x12M\n\x1cuser_deco_pins_inventory_map\x18N \x01(\x0b\x32\'.krdori.pb2.ce.UserDecoPinsInventoryMap\x12=\n\x13user_deco_equipment\x18O \x01(\x0b\x32 .krdori.pb2.ce.UserDecoEquipment\x12Z\n#user_music_video_inventory_list_map\x18V \x01(\x0b\x32-.krdori.pb2.ce.UserMusicVideoInventoryListMap\x12G\n\x19user_music_video_list_map\x18W \x01(\x0b\x32$.krdori.pb2.ce.UserMusicVideoListMap\x12V\n!user_purchase_menu_last_visit_map\x18X \x01(\x0b\x32+.krdori.pb2.ce.UserPurchaseMenuLastVisitMap\x12:\n\x12user_skin_lane_map\x18Y \x01(\x0b\x32\x1e.krdori.pb2.ce.UserSkinLaneMap\x12S\n#current_user_event_music_scores_map\x18\x65 \x01(\x0b\x32&.krdori.pb2.ce.UserEventMusicScoresMap\x12_\n)current_user_event_music_achievements_map\x18\x66 \x01(\x0b\x32,.krdori.pb2.ce.UserEventMusicAchievementsMap\x12M\n current_user_event_box_gacha_map\x18g \x01(\x0b\x32#.krdori.pb2.ce.UserEventBoxGachaMap\x12H\n\x19user_monthly_purchase_map\x18i \x01(\x0b\x32%.krdori.pb2.ce.UserMonthlyPurchaseMap\x12\x43\n\x16user_subscription_list\x18j \x01(\x0b\x32#.krdori.pb2.ce.UserSubscriptionList\x12\x46\n\x18user_comment_banner_list\x18l \x01(\x0b\x32$.krdori.pb2.ce.UserCommentBannerList\x12X\n\"user_event_box_gacha_spin_settings\x18n \x01(\x0b\x32,.krdori.pb2.ce.UserEventBoxGachaSpinSettings\x12\x44\n\x19user_morfonica_story_list\x18\xc9\x01 \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12G\n\x18user_matching_bonus_list\x18\xca\x01 \x01(\x0b\x32$.krdori.pb2.ce.UserMatchingBonusList\x12I\n\x1euser_raise_a_suilen_story_list\x18\xcc\x01 \x01(\x0b\x32 .krdori.pb2.ce.UserBandStoryList\x12P\n%user_collabo_original_music_score_map\x18\xcd\x01 \x01(\x0b\x32 .krdori.pb2.ce.UserMusicScoreMap\x12\x36\n\x0fuser_daily_live\x18\xce\x01 \x01(\x0b\x32\x1c.krdori.pb2.ce.UserDailyLive\x12]\n$user_daily_live_total_reward_history\x18\xcf\x01 \x01(\x0b\x32..krdori.pb2.ce.UserDailyLiveTotalRewardHistory\x12@\n\x14user_comeback_status\x18\xd2\x01 \x01(\x0b\x32!.krdori.pb2.ce.UserComebackStatus\x12U\n\x1fuser_graphical_information_list\x18\xd3\x01 \x01(\x0b\x32+.krdori.pb2.ce.UserGraphicalInformationList\x12W\n!user_multi_live_count_reward_list\x18\xd4\x01 \x01(\x0b\x32+.krdori.pb2.ce.UserMultiLiveCountRewardList\x12\x43\n\x16user_digest_story_list\x18\xd5\x01 \x01(\x0b\x32\".krdori.pb2.ce.UserDigestStoryList\x12\\\n$user_live_boost_use_bonus_limit_list\x18\xd6\x01 \x01(\x0b\x32-.krdori.pb2.ce.UserLiveBoostUseBonusLimitList\x12`\n%user_receivable_present_location_list\x18\xd7\x01 \x01(\x0b\x32\x30.krdori.pb2.ce.UserReceivablePresentLocationList\x12\x45\n\x17user_panel_mission_list\x18\xdc\x01 \x01(\x0b\x32#.krdori.pb2.ce.UserPanelMissionList\x12S\n\x1euser_birthday_introduction_map\x18\xe2\x01 \x01(\x0b\x32*.krdori.pb2.ce.UserBirthdayIntroductionMap\x12\x43\n\x16user_festival_team_map\x18\xe9\x01 \x01(\x0b\x32\".krdori.pb2.ce.UserFestivalTeamMap\x12\x43\n\x16user_limited_item_list\x18\xf1\x01 \x01(\x0b\x32\".krdori.pb2.ce.UserLimitedItemList\x12M\n\x1buser_limited_exchanges_list\x18\xf2\x01 \x01(\x0b\x32\'.krdori.pb2.ce.UserLimitedExchangesList\x12\x34\n\x0euser_deck_list\x18\xf3\x01 \x01(\x0b\x32\x1b.krdori.pb2.ce.UserDeckList\x12k\n+user_add_music_difficulty_introduction_list\x18\xfb\x01 \x01(\x0b\x32\x35.krdori.pb2.ce.UserAddMusicDifficultyIntroductionList\x12:\n\x11user_gallery_list\x18\xfc\x01 \x01(\x0b\x32\x1e.krdori.pb2.ce.UserGalleryList\x12H\n\x19user_band_deck_rating_map\x18\xfd\x01 \x01(\x0b\x32$.krdori.pb2.ce.UserBandDeckRatingMap\x12L\n\x1bupdated_band_deck_rank_list\x18\xfe\x01 \x01(\x0b\x32&.krdori.pb2.ce.UpdatedBandDeckRankList\x12W\n!user_stage_challenge_stage_no_map\x18\x84\x02 \x01(\x0b\x32+.krdori.pb2.ce.UserStageChallengeStageNoMap\x12G\n\x18user_stage_challenge_map\x18\x85\x02 \x01(\x0b\x32$.krdori.pb2.ce.UserStageChallengeMap\x12R\n\x1euser_stage_challenge_score_map\x18\x86\x02 \x01(\x0b\x32).krdori.pb2.ce.UserStageChallengeScoreMap\x12\x34\n\x0euser_star_seal\x18\x8e\x02 \x01(\x0b\x32\x1b.krdori.pb2.ce.UserStarSeal\x12\x46\n\x18user_live_boost_use_full\x18\x8f\x02 \x01(\x0b\x32#.krdori.pb2.ce.UserLiveBoostUseFull\x12\x34\n\x0euser_auto_live\x18\x98\x02 \x01(\x0b\x32\x1b.krdori.pb2.ce.UserAutoLive\x12@\n\x14user_monthly_mission\x18\xa2\x02 \x01(\x0b\x32!.krdori.pb2.ce.UserMonthlyMission\x12V\n user_monthly_mission_reward_list\x18\xa3\x02 \x01(\x0b\x32+.krdori.pb2.ce.UserMonthlyMissionRewardListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.suite_user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SUITEUSERGETRESPONSE']._serialized_start=3765
  _globals['_SUITEUSERGETRESPONSE']._serialized_end=11881
# @@protoc_insertion_point(module_scope)
