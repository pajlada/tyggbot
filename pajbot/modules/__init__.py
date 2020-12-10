from pajbot.modules.base import BaseModule
from pajbot.modules.base import ModuleSetting
from pajbot.modules.base import ModuleType

from pajbot.modules.ascii import AsciiProtectionModule
from pajbot.modules.banphrase import BanphraseModule
from pajbot.modules.basic import BasicCommandsModule
from pajbot.modules.basic.ab import AbCommandModule
from pajbot.modules.basic.admincommands import AdminCommandsModule
from pajbot.modules.basic.checkmod import CheckModModule
from pajbot.modules.basic.clip import ClipCommandModule
from pajbot.modules.basic.dbmanage import DBManageModule
from pajbot.modules.basic.debug import DebugModule
from pajbot.modules.basic.emotes import EmotesModule
from pajbot.modules.basic.followage import FollowAgeModule
from pajbot.modules.basic.ignore import IgnoreModule
from pajbot.modules.basic.permaban import PermabanModule
from pajbot.modules.basic.pointsreset import PointsResetModule
from pajbot.modules.basic.stream_update import StreamUpdateModule
from pajbot.modules.bingo import BingoModule
from pajbot.modules.casechecker import CaseCheckerModule
from pajbot.modules.chat_alerts import ChatAlertModule
from pajbot.modules.chat_alerts.livealert import LiveAlertModule
from pajbot.modules.chat_alerts.newchatteralert import NewChatterAlertModule
from pajbot.modules.chat_alerts.subalert import SubAlertModule
from pajbot.modules.chat_alerts.raidalert import RaidAlertModule
from pajbot.modules.chatters_refresh import ChattersRefreshModule
from pajbot.modules.deck import DeckModule
from pajbot.modules.duel import DuelModule
from pajbot.modules.dummy import DummyModule
from pajbot.modules.eightball import EightBallModule
from pajbot.modules.emote_timeout import EmoteTimeoutModule
from pajbot.modules.emote_limit import EmoteLimitModule
from pajbot.modules.emotecombo import EmoteComboModule
from pajbot.modules.emotesonscreen import EmotesOnScreenModule
from pajbot.modules.givepoints import GivePointsModule
from pajbot.modules.hsbet import HSBetModule
from pajbot.modules.lastfm import LastfmModule
from pajbot.modules.leaguerank import LeagueRankModule
from pajbot.modules.linefarming import LineFarmingModule
from pajbot.modules.linkchecker import BlacklistedLink
from pajbot.modules.linkchecker import LinkCheckerModule
from pajbot.modules.linkchecker import WhitelistedLink
from pajbot.modules.linktracker import LinkTrackerLink
from pajbot.modules.linktracker import LinkTrackerModule
from pajbot.modules.massping import MassPingProtectionModule
from pajbot.modules.math import MathModule
from pajbot.modules.maxmsglength import MaxMsgLengthModule
from pajbot.modules.moderators_refresh import ModeratorsRefreshModule
from pajbot.modules.paidsubmode import PaidSubmodeModule
from pajbot.modules.paidtimeout import PaidTimeoutModule
from pajbot.modules.paiduntimeout import PaidUntimeoutModule
from pajbot.modules.playsound import PlaysoundModule
from pajbot.modules.pnsl import PNSLModule
from pajbot.modules.pointlottery import PointLotteryModule
from pajbot.modules.predict import PredictModule
from pajbot.modules.pyramid import PyramidModule
from pajbot.modules.quest import QuestModule
from pajbot.modules.quests.gettimedout import GetTimedOutQuestModule
from pajbot.modules.quests.typeemote import TypeEmoteQuestModule
from pajbot.modules.quests.typememessage import TypeMeMessageQuestModule
from pajbot.modules.quests.winduelpoints import WinDuelPointsQuestModule
from pajbot.modules.quests.winduels import WinDuelsQuestModule
from pajbot.modules.quests.winhsbetpoints import WinHsBetPointsQuestModule
from pajbot.modules.quests.winhsbetwins import WinHsBetWinsQuestModule
from pajbot.modules.quests.winraffle import WinRaffleQuestModule
from pajbot.modules.raffle import RaffleModule
from pajbot.modules.repspam import RepspamModule
from pajbot.modules.roulette import RouletteModule
from pajbot.modules.showemote import ShowEmoteModule
from pajbot.modules.slotmachine import SlotMachineModule
from pajbot.modules.subscriber_fetch import SubscriberFetchModule
from pajbot.modules.top import TopModule
from pajbot.modules.trivia import TriviaModule
from pajbot.modules.vanish import VanishModule
from pajbot.modules.vip_refresh import VIPRefreshModule
from pajbot.modules.warning import WarningModule
from pajbot.modules.wolfram import WolframModule

from pajbot.modules.analogy import AnalogyModule
from pajbot.modules.bet import BetModule
from pajbot.modules.convert_points import ConvertPoints
from pajbot.modules.spotify_streamlabs import SpotifyStreamLabs
from pajbot.modules.spotifyquery import SpotifySongQuery
from pajbot.modules.reward_tts_amazon import RewardTTSModuleAmazon
from pajbot.modules.reward_tts_streamlabs import RewardTTSModuleStreamLabs
from pajbot.modules.random_redeem_points import RandomRedeem
from pajbot.modules.taxation import TaxationModule
from pajbot.modules.channel_point_timeout import ChannelPointTimeout
from pajbot.modules.songrequest import SongrequestModule
from pajbot.modules.convert_points import ConvertPoints

available_modules = [
    AnalogyModule,
    AbCommandModule,
    AdminCommandsModule,
    AsciiProtectionModule,
    BanphraseModule,
    BasicCommandsModule,
    BetModule,
    BingoModule,
    CaseCheckerModule,
    ChatAlertModule,
    ChattersRefreshModule,
    CheckModModule,
    ClipCommandModule,
    ConvertPoints,
    DBManageModule,
    DebugModule,
    DeckModule,
    DuelModule,
    DummyModule,
    EightBallModule,
    EmoteComboModule,
    EmoteLimitModule,
    EmoteTimeoutModule,
    EmotesModule,
    EmotesOnScreenModule,
    FollowAgeModule,
    GetTimedOutQuestModule,
    GivePointsModule,
    HSBetModule,
    IgnoreModule,
    LastfmModule,
    LeagueRankModule,
    LineFarmingModule,
    LinkCheckerModule,
    LinkTrackerModule,
    LiveAlertModule,
    MassPingProtectionModule,
    MathModule,
    MaxMsgLengthModule,
    ModeratorsRefreshModule,
    NewChatterAlertModule,
    PNSLModule,
    PaidSubmodeModule,
    PaidTimeoutModule,
    PaidUntimeoutModule,
    PermabanModule,
    PlaysoundModule,
    PointLotteryModule,
    PointsResetModule,
    PredictModule,
    PyramidModule,
    QuestModule,
    RaffleModule,
    RaidAlertModule,
    RandomRedeem,
    RepspamModule,
    RewardTTSModuleAmazon,
    RewardTTSModuleStreamLabs,
    RouletteModule,
    ShowEmoteModule,
    SlotMachineModule,
    SongrequestModule,
    SpotifyStreamLabs,
    SpotifySongQuery,
    StreamUpdateModule,
    SubAlertModule,
    SubscriberFetchModule,
    TaxationModule,
    TopModule,
    TriviaModule,
    TypeEmoteQuestModule,
    TypeMeMessageQuestModule,
    VanishModule,
    VIPRefreshModule,
    WarningModule,
    WinDuelPointsQuestModule,
    WinDuelsQuestModule,
    WinHsBetPointsQuestModule,
    WinHsBetWinsQuestModule,
    WinRaffleQuestModule,
    WolframModule,
]
