using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003092: Franz
/// </summary>
public class _11003092 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0113173307007775$
    // - Hello, how may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0113173307007778$
                // - Hello, how may I help you?
                switch (selection) {
                    // $script:0113173307007779$
                    // - How can I play music in $map:02000064$?
                    case 0:
                        return 31;
                    // $script:0113173307007780$
                    // - How can I get to the stage?
                    case 1:
                        return 33;
                    // $script:0113173307007781$
                    // - How can I cheer during a performance?
                    case 2:
                        return 34;
                }
                return -1;
            case (31, 0):
                // $script:0113173307007782$
                // - All you have to do to perform in $map:02000064$ is apply! Just press the request button. If someone else has already applied, you'll need to wait 10 minutes and then apply again when they're done.
                switch (selection) {
                    // $script:0113173307007783$
                    // - How can I play as a group?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0113173307007784$
                // - For ensemble performances, form a party with someone who has applied to perform. After that you can all take the stage together.
                return 32;
            case (32, 1):
                // $script:0113173307007785$
                // - It's super easy to perform in a group! So, is there anything else you want to know?
                switch (selection) {
                    // $script:0113173307007786$
                    // - How can I get to the stage?
                    case 0:
                        return 33;
                    // $script:0113173307007787$
                    // - How can I cheer during a performance?
                    case 1:
                        return 34;
                    // $script:0113173307007788$
                    // - No, I think I'm good.
                    case 2:
                        return 35;
                }
                return -1;
            case (33, 0):
                // $script:0113173307007789$
                // - We'll let you up on stage if you're going to perform. Just hit the apply button and we'll let you know when it's time.
                return 33;
            case (33, 1):
                // $script:0113173307007790$
                // - If you want to leave the stage, just hit the same button you used to get up there. That was an easy one. Anything else?
                switch (selection) {
                    // $script:0113173307007791$
                    // - How can I play music in $map:02000064$?
                    case 0:
                        return 31;
                    // $script:0113173307007792$
                    // - How can I cheer during a performance?
                    case 1:
                        return 34;
                    // $script:0113173307007793$
                    // - No, I think I'm good.
                    case 2:
                        return 35;
                }
                return -1;
            case (34, 0):
                // $script:0113173307007794$
                // - Everyone in $map:02000064$ can hear performances from the stage. Show your appreciation by lighting firecrackers, waving glowsticks, or just clapping!
                return 34;
            case (34, 1):
                // $script:0113173307007795$
                // - Cheers and applause encourage the performers, so let 'em have it! Anything else you want to know?
                switch (selection) {
                    // $script:0113173307007796$
                    // - How can I play music in $map:02000064$?
                    case 0:
                        return 31;
                    // $script:0113173307007797$
                    // - How can I get to the stage?
                    case 1:
                        return 33;
                    // $script:0113173307007798$
                    // - No, I think I'm good.
                    case 2:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0113173307007799$
                // - Great! Come on back if you have any more questions about performing in $map:02000064$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
