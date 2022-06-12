using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001108: Lennon
/// </summary>
public class _11001108 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003723$
    // - How did you get here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003726$
                // - $npcName:11000614[gender:0]$ and I met in Katramus. I can't believe we were able to meet again here. I'm also glad that his sister is safe!
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
