using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000243: Laura
/// </summary>
public class _11000243 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001028$
    // - Oh, can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001031$
                // - I don't know what to do... I think he's interested in me!
                switch (selection) {
                    // $script:0831180407001032$
                    // - I'm not really interested in you, sorry.
                    case 0:
                        return 21;
                    // $script:0831180407001033$
                    // - Who are you talking about?
                    case 1:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:0831180407001034$
                // - Well... good! I'm not interested in you either, $MyPCName$.
                return -1;
            case (22, 0):
                // $script:0831180407001035$
                // - That guy over there, the tired one... Do you know that feeling you get when you make eye contact with someone special?
                return 22;
            case (22, 1):
                // $script:0831180407001036$
                // - Eeeee! What do I do?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Next,
            (22, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
