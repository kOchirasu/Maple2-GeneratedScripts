using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001686: Zabeth
/// </summary>
public class _11001686 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006484$
    // - What're you staring at? You want a piece of me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006487$
                // - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
                switch (selection) {
                    // $script:0706173707006645$
                    // - What's your rank in Blackstar?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0706173707006646$
                // - I'm a henchman, plain and simple. $npcName:11001678[gender:0]$ has big ideas about moving up in the organization, but I don't care what they call me as long as I get to bash heads in.
                return 40;
            case (40, 1):
                // $script:0706173707006647$
                // - Boss. Lackey. It doesn't matter. All that matters is how strong you are. $npcName:11001678[gender:0]$ can try to rise as much as he wants, but he's got a glass jaw. A weakling like him just ain't officer material.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
