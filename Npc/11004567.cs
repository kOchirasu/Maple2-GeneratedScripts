using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004567: Vasara Chen
/// </summary>
public class _11004567 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0220211107014547$
    // - Really?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014548$
                // - Hm?
                return 10;
            case (10, 1):
                // $script:0220211107014549$
                // - You look strong. Almost as strong as someone I know...
                switch (selection) {
                    // $script:0220211107014550$
                    // - You're one to talk.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0220211107014551$
                // - Hey, you ever hear of the Gray Wolf?
                switch (selection) {
                    // $script:0220211107014552$
                    // - I may have heard the name.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0220211107014553$
                // - I have a feeling the Gray Wolf will be here. We've got unfinished business...
                return -1;
            case (20, 0):
                // $script:0220211107014554$
                // - Hey, Gray Wolf.
                switch (selection) {
                    // $script:0220211107014555$
                    // - Vasara Chen?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0220211107014556$
                // - I knew you'd be here. A fighter like you can't resist the ring for long.
                return 21;
            case (21, 1):
                // $script:0220211107014557$
                // - That's why I signed up. Figured it's a good chance for us to duke it out.
                switch (selection) {
                    // $script:0220211107014558$
                    // - This is getting interesting.
                    case 0:
                        return 22;
                }
                return -1;
            case (22, 0):
                // $script:0220211107014559$
                // - I hope you haven't slacked off in your training. I haven't.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
