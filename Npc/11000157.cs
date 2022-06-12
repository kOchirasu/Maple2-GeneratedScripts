using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000157: Paul
/// </summary>
public class _11000157 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000663$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000665$
                // - I don't know what caused the recent earthquake. It was so strong, it tore the Royal Road in half. This could be a serious problem.
                return -1;
            case (30, 0):
                // $script:0116162507009762$
                // - It's really you! $MyPCName$, in the flesh!
                return 30;
            case (30, 1):
                // $script:0116162507009763$
                // - It's an honor to meet you!
                switch (selection) {
                    // $script:0116162507009764$
                    // - You know me?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0116162507009765$
                // - You're the hero of the Siege of $map:02000001$. Of course I know you! You're a hero to all of us here.
                switch (selection) {
                    // $script:0116162507009766$
                    // - I was just doing my duty.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0116162507009767$
                // - You're so humble. Wow! Listen, if there's anything I can do to help you, just say the word.
                switch (selection) {
                    // $script:0116162507009768$
                    // - I'm looking into rumors about hot places. Like, super hot.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0116162507009769$
                // - Hot places, huh? Like unseasonably hot places?
                switch (selection) {
                    // $script:0116162507009770$
                    // - That's one example.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0116162507009771$
                // - Now that you mention it, I did hear a rumor from one of the merchants with the Barrota Trading Company. You heard about their new air trade routes, didn't you?
                switch (selection) {
                    // $script:0116162507009772$
                    // - I may have heard a thing or two.
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0116162507009773$
                // - Well, a few of their routes pass over the ruins of Orbis. They say that the airships passing through the area get so hot, you can fry an egg on their decks.
                return 35;
            case (35, 1):
                // $script:0116162507009774$
                // - Interesting, right?
                switch (selection) {
                    // $script:0116162507009775$
                    // - Fascinating.
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:0116170407009788$
                // - That's all I know.
                switch (selection) {
                    // $script:0116170407009789$
                    // - It was a big help.
                    case 0:
                        return 37;
                }
                return -1;
            case (37, 0):
                // $script:0116162507009776$
                // - I can't believe <i>I</i> am getting to talk to <i>you</i> about real important official business! Don't worry, $male:sir,female:ma'am$, I'll do my best to keep $map:02000001$ safe, too!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Next,
            (35, 1) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.SelectableDistractor,
            (37, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
