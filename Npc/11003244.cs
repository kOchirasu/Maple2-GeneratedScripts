using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003244: Armano
/// </summary>
public class _11003244 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008147$
    // - No... This c-can't...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008149$
                // - Not this... Anything but this...
                //   <font color="#909090">($npcName:11003240[gender:0]$ lowers his head, his shoulders trembling ever so slightly.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
