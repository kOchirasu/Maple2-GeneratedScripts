using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001601: Jenna
/// </summary>
public class _11001601 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006089$
    // - Do you have business with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006138$
                // - The real fun is about to begin! I'm going to blow that $npcName:11001231[gender:0]$ guy to smithereens!
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
