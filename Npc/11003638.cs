using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003638: Fabien
/// </summary>
public class _11003638 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009095$
    // - Wow! This place is amazing.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009096$
                // - Excuse me! Would you mind taking my picture?
                switch (selection) {
                    // $script:1109121007009097$
                    // - Sure, I'll take one for you.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009098$
                // - Okay, great! Now, I'll just pose like this and you pretend you're taking a snapshot like that... And let $npcName:11003535[gender:1]$ know that I say, "Nya-nyah-nya-nya-nyah!"
                switch (selection) {
                    // $script:1109121007009099$
                    // - Uh...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009100$
                // - Act natural! And be sure to let $npcName:11003535[gender:1]$ know my exact words. Mess this up and the whole operation is done for.
                switch (selection) {
                    // $script:1109121007009101$
                    // - Understood.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009102$
                // - Wow! The picture came out great. Thank you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
