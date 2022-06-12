using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003196: Katvan
/// </summary>
public class _11003196 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0404083307008224$
    // - $npcName:11003216[gender:0]$... That fool!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008225$
                // - I won't give up until $npcName:11003216[gender:0]$ pays for his crimes. I just wish $npcName:11000069[gender:1]$ would understand that I'm doing this for her...
                return -1;
            case (20, 0):
                // $script:0516084007008486$
                // - I told you! As long as $npcName:11003216[gender:0]$ is alive, $npcName:11000069[gender:1]$ isn't safe.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
