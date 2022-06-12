using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003262: Kaitlyn
/// </summary>
public class _11003262 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008202$
    // - Professor $npcName:11003251[gender:0]$... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008203$
                // - Where is he? I have to find him. He isn't himself!
                switch (selection) {
                    // $script:0403155707008204$
                    // - What do you know about this?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0403155707008205$
                // - N-nothing! I... I don't know anything...
                //   <font color="#909090">($npcName:11003146[gender:1]$ shakes her head in frustration.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
