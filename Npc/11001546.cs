using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001546: Zabeth
/// </summary>
public class _11001546 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0516130207006114$
    // - What're you looking at? You got something to say?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0531170907006244$
                // - <font color="#909090">($npc:11001546[gender:0]$ scowls at you.)</font>
                switch (selection) {
                    // $script:0531170907006245$
                    // - Um... Can I help you?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0531170907006246$
                // - Go back to your corner and practice. I'm busy.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
