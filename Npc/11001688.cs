using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001688: Zabeth
/// </summary>
public class _11001688 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006492$
    // - What're you staring at? You want a piece of me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006495$
                // - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
                switch (selection) {
                    // $script:0706173707006650$
                    // - What was that clone in the video?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0706173707006651$
                // - I don't know if it was a clone or just someone who really looks like $npcName:11001680[gender:0]$. And I don't want to know. Now stop making me think about it.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
