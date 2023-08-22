"""Wrapper For Click"""
from gettext import gettext as _

import click


class File(click.Path):
    def __init__(self, *args, **kwargs):
        super().__init__(
            exists=True, dir_okay=False, resolve_path=True,
            *args, **kwargs)


class Directory(click.Path):
    def __init__(self, *args, **kwargs):
        super().__init__(
            exists=True, file_okay=False, resolve_path=True,
            *args, **kwargs)


class Command(click.Command):
    def get_help_option(self, ctx):
        option = super().get_help_option(ctx)
        option.help = _("Mostra essa mensagem e termina.")
        return option


class Group(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(
            context_settings={
                "help_option_names": ["-h", "--help"],
                "max_content_width": 100},
            *args, **kwargs)

    def get_help_option(self, ctx):
        option = super().get_help_option(ctx)
        option.help = _("Mostra essa mensagem e termina.")
        return option

    def format_commands(self, ctx, formatter):
        groups = []
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)

            if cmd is None:
                continue
            if cmd.hidden:
                continue

            if isinstance(cmd, click.Group):
                groups.append((subcommand, cmd))
            else:
                commands.append((subcommand, cmd))

        if groups:
            self.write_commands(formatter, "General Commands", commands)
            self.write_commands(formatter, "Companies Commands", groups)
        else:
            self.write_commands(formatter, "Commands", commands)

    @staticmethod
    def write_commands(formatter, section, commands):
        if len(commands):
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)

            rows = []
            for subcommand, cmd in commands:
                help_ = cmd.get_short_help_str(limit)
                rows.append((subcommand, help_))

            if rows:
                with formatter.section(_(section)):
                    formatter.write_dl(rows)


def command(*args, **kwargs):
    return click.command(cls=Command, *args, **kwargs)


def group(*args, **kwargs):
    return click.group(cls=Group, *args, **kwargs)
