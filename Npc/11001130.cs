using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001130: Nordan
/// </summary>
public class _11001130 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003858$
    // - D-do you want some herbs?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003861$
                // - W-what's with those weird noises? You hear them too, r-right?
                switch (selection) {
                    // $script:0911192907003862$
                    // - I didn't hear anything.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0911192907003863$
                // - What?! D-don't look at me like that... I'm not crazy!
                switch (selection) {
                    // $script:0911192907003864$
                    // - It was probably just a small animal.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0911192907003865$
                // - Y-you think so? You'll protect me if it's something scary though, right? Hngg... Now my heart is p-pounding.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
