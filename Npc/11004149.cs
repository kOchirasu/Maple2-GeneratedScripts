using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004149: Terry
/// </summary>
public class _11004149 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010569$
    // - Hm hm hmmm, hm! Those marching songs always get stuck in my head.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010570$
                // - I've loved $npcName:11000444[gender:0]$'s books and the sea ever since I was a boy—probably a side-effect of growing up by the ocean. And now I'm on a voyage of my own, alongside my childhood friends.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
