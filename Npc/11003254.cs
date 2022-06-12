using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003254: Kaitlyn
/// </summary>
public class _11003254 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008175$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008176$
                // - I don't know what you did to impress $npcName:11003250[gender:0]$, but I'm not convinced. So, how are you going to prove that you're worth my time? 
                return 30;
            case (30, 1):
                // $script:0403155707008177$
                // - <font color="#909090">($npc:11003254[gender:1]$'s voice drops to a whisper.)</font>
                //   <font size='20'>This is all for Professor $npc:11003148[gender:0]$...</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
