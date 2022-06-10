using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001479: Startz
/// </summary>
public class _11001479 : NpcScript {
    internal _11001479(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005765$ 
                // - Do you have something to say to me?
                return true;
            case 10:
                // $script:0106111607005766$ 
                // - I'm glad we've retrieved the Lumenstone, but the war with the Kargons is far from over.
                return true;
            default:
                return true;
        }
    }
}
