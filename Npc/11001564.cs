using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001564: Eupheria
/// </summary>
public class _11001564 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006052$
    // - There you are.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006108$
                // - No matter $npcName:11001231[gender:0]$'s reasons or excuses, I will never forgive him for murdering Arazaad.
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
