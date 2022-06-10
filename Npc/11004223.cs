using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004223: Rinet
/// </summary>
public class _11004223 : NpcScript {
    internal _11004223(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010794$ 
                // - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
                return true;
            case 10:
                // $script:0806222707010795$ 
                // - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
                return true;
            default:
                return true;
        }
    }
}
