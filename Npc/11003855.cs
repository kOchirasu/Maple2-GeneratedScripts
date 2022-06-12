using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003855: 
/// </summary>
public class _11003855 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.Next);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1130175706001007$ 
                // - I've got everything you need to take on $npc:23000090[gender:0]$.
                return default;
            case 30:
                switch (Index++) {
                    case 0:
                        // $script:1130175706001008$ 
                        // - The particle cannon is our last hope. $MyPCName$, I leave it to you!
                        return (30, NpcTalkButton.Close);
                    case 1:
                        // $script:1130175706001009$ 
                        // - Look alive! $npc:23000090[gender:0]$ is out there!
                        return default;
                }
                break;
        }
        
        return default;
    }
}
