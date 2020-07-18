import logging

from pajbot.managers.emote import BTTVEmoteManager, FFZEmoteManager, TwitchEmoteManager
from pajbot.models.command import Command
from pajbot.models.command import CommandExample
from pajbot.modules import BaseModule
from pajbot.modules import ModuleSetting
from pajbot.modules.basic import BasicCommandsModule
from pajbot.streamhelper import StreamHelper
from pajbot.utils import split_into_chunks_with_prefix

log = logging.getLogger(__name__)


class EmotesModule(BaseModule):
    ID = __name__.split(".")[-1]
    NAME = "Emotes"
    ENABLED_DEFAULT = True
    DESCRIPTION = "Refresh and list FFZ, BTTV and Sub emotes"
    CATEGORY = "Feature"
    PARENT_MODULE = BasicCommandsModule
    SETTINGS = [
        ModuleSetting(
            key="global_cd",
            label="Global cooldown of all emote-commands (seconds)",
            type="number",
            required=True,
            placeholder="",
            default=5,
            constraints={"min_value": 0, "max_value": 120},
        ),
        ModuleSetting(
            key="user_cd",
            label="Per-user cooldown of all emote-commands (seconds)",
            type="number",
            required=True,
            placeholder="",
            default=15,
            constraints={"min_value": 0, "max_value": 240},
        ),
        ModuleSetting(
            key="level",
            label="Level required to use the commands",
            type="number",
            required=True,
            placeholder="",
            default=100,
            constraints={"min_value": 100, "max_value": 2000},
        ),
        ModuleSetting(
            key="enable_subemotes", label="Enable !subemotes command", type="boolean", required=True, default=True
        ),
        ModuleSetting(
            key="custom_sub_response",
            label="Enable a custom response to the !subemotes command. Leave empty to disable the message. | Available arguments: {source}, {streamer}",
            type="text",
            required=False,
            placeholder="@{source}, Channel sub emotes can be found here: https://twitchemotes.com/channels/11148817",
            default="",
            constraints={"max_str_len": 400},
        ),
        ModuleSetting(
            key="enable_ffzemotes", label="Enable !ffzemotes command", type="boolean", required=True, default=True
        ),
        ModuleSetting(
            key="custom_ffz_response",
            label="Enable a custom response to the !ffzemotes command. Leave empty to disable the message. | Available arguments: {source}, {streamer}",
            type="text",
            required=False,
            placeholder="@{source}, Channel FFZ emotes can be found here: https://www.frankerfacez.com/channel/pajlada",
            default="",
            constraints={"max_str_len": 400},
        ),
        ModuleSetting(
            key="enable_bttvemotes", label="Enable !bttvemotes command", type="boolean", required=True, default=True
        ),
        ModuleSetting(
            key="custom_bttv_response",
            label="Enable a custom response to the !bttvemotes command. Leave empty to disable the message. | Available arguments: {source}, {streamer}",
            type="text",
            required=False,
            placeholder="@{source}, Channel BTTV emotes can be found here: https://betterttv.com/users/550daf6562e6bd0027aedb5e",
            default="",
            constraints={"max_str_len": 400},
        ),
    ]

    def print_emotes(self, source, manager):
        emotes = manager.channel_emotes
        streamer = self.bot.streamer_display
        messages = split_into_chunks_with_prefix(
            [{"prefix": f"{manager.friendly_name} emotes:", "parts": [e.code for e in emotes]}],
            default=f"No {manager.friendly_name} Emotes active in this chat :(",
        )

        if self.settings[f"custom_{manager.friendly_name.lower()}_response"] != "":
            custom_message = self.settings[f"custom_{manager.friendly_name.lower()}_response"]

        if custom_message == "":
            for message in messages:
                self.bot.say(message)
        else:
            self.bot.say(custom_message.format(streamer=streamer, source=source))

    def print_twitch_emotes(self, source, **rest):
        manager = self.bot.emote_manager.twitch_emote_manager
        streamer = self.bot.streamer_display
        messages = split_into_chunks_with_prefix(
            [
                {"prefix": "Subscriber emotes:", "parts": [e.code for e in manager.tier_one_emotes]},
                {"prefix": "T2:", "parts": [e.code for e in manager.tier_two_emotes]},
                {"prefix": "T3:", "parts": [e.code for e in manager.tier_three_emotes]},
            ],
            default=f"Looks like {StreamHelper.get_streamer()} has no subscriber emotes! :(",
        )

        if self.settings["custom_sub_response"] != "":
            streamer = self.bot.streamer_display
            custom_message = self.settings["custom_sub_response"]
            self.bot.say(custom_message.format(streamer=streamer, source=source))
        else:
            manager = self.bot.emote_manager.twitch_emote_manager

            messages = split_into_chunks_with_prefix(
                [
                    {"prefix": "Subscriber emotes:", "parts": [e.code for e in manager.tier_one_emotes]},
                    {"prefix": "T2:", "parts": [e.code for e in manager.tier_two_emotes]},
                    {"prefix": "T3:", "parts": [e.code for e in manager.tier_three_emotes]},
                ],
                default=f"Looks like {StreamHelper.get_streamer()} has no subscriber emotes! :(",
            )

            for message in messages:
                self.bot.say(message)            

    def reload_cmd(self, manager):
        # manager is an instance of the manager in the bot and the class of the manager on the web interface
        reload_msg = f"Reloading {manager.friendly_name} emotes..."

        def do_reload(bot, source, **rest):
            bot.whisper(source, reload_msg)
            self.bot.action_queue.submit(manager.update_all)

        return Command.raw_command(
            do_reload,
            level=500,
            delay_all=10,
            delay_user=20,
            examples=[
                CommandExample(
                    None,
                    f"Reload all active {manager.friendly_name} emotes for this channel.",
                    chat=f"user: !{manager.friendly_name.lower()}emotes reload\n" + f"bot>user: {reload_msg}",
                ).parse()
            ],
        )

    def print_cmd(self, manager, examples):
        def do_print(bot, source, **rest):
            self.print_emotes(source, manager)

        return Command.raw_command(
            do_print,
            level=100,
            delay_all=15,
            delay_user=30,
            examples=[
                CommandExample(
                    None,
                    f"Show all active {manager.friendly_name} emotes for this channel.",
                    chat=f"user: !{manager.friendly_name.lower()}emotes\n"
                    + f"bot: {manager.friendly_name} emotes: {examples}",
                ).parse()
            ],
        )

    def print_twitch_cmd(self):
        return Command.raw_command(
            self.print_twitch_emotes,
            level=100,
            delay_all=15,
            delay_user=30,
            examples=[
                CommandExample(
                    None,
                    f"Show all active sub emotes for {StreamHelper.get_streamer()}.",
                    chat="user: !subemotes\n"
                    "bot: Subscriber emotes: forsenE forsenC forsenK forsenW "
                    "Tier 2: forsenSnus Tier 3: forsen2499",
                ).parse()
            ],
        )

    def load_commands(self, **options):
        cmd_reload_bttv_emotes = self.reload_cmd(
            self.bot.emote_manager.bttv_emote_manager if self.bot else BTTVEmoteManager
        )
        cmd_reload_ffz_emotes = self.reload_cmd(
            self.bot.emote_manager.ffz_emote_manager if self.bot else FFZEmoteManager
        )
        cmd_reload_twitch_emotes = self.reload_cmd(
            self.bot.emote_manager.twitch_emote_manager if self.bot else TwitchEmoteManager
        )
        cmd_print_bttv_emotes = self.print_cmd(
            self.bot.emote_manager.bttv_emote_manager if self.bot else BTTVEmoteManager, "forsenPls gachiGASM"
        )
        cmd_print_ffz_emotes = self.print_cmd(
            self.bot.emote_manager.ffz_emote_manager if self.bot else FFZEmoteManager, "FeelsOkayMan Kapp LULW"
        )

        # The ' ' is there to make things look good in the
        # web interface.
        if self.settings["enable_bttvemotes"]:
            self.commands["bttvemotes"] = Command.multiaction_command(
                delay_all=self.settings["global_cd"],
                delay_user=self.settings["user_cd"],
                level=self.settings["level"],
                default=" ",
                fallback=" ",
                command="bttvemotes",
                commands={"reload": cmd_reload_bttv_emotes, " ": cmd_print_bttv_emotes},
            )

        if self.settings["enable_ffzemotes"]:
            self.commands["ffzemotes"] = Command.multiaction_command(
                delay_all=self.settings["global_cd"],
                delay_user=self.settings["user_cd"],
                level=self.settings["level"],
                default=" ",
                fallback=" ",
                command="ffzemotes",
                commands={"reload": cmd_reload_ffz_emotes, " ": cmd_print_ffz_emotes},
            )

        if self.settings["enable_subemotes"]:
            self.commands["subemotes"] = Command.multiaction_command(
                delay_all=self.settings["global_cd"],
                delay_user=self.settings["user_cd"],
                level=self.settings["level"],
                default=" ",
                fallback=" ",
                command="subemotes",
                commands={"reload": cmd_reload_twitch_emotes, " ": self.print_twitch_cmd()},
            )
