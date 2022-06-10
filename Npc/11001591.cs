using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001591: Einos
/// </summary>
public class _11001591 : NpcScript {
    internal _11001591(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006079$ 
                // - Hello.
                return true;
            case 10:
                // $script:0515180307006130$ 
                // - $npcName:11001229[gender:0]$ is strong. He'll recover. Until then, the Life Lapenta will protect him.
                return true;
            default:
                return true;
        }
    }
}
