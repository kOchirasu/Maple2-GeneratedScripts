using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000030: Robin
/// </summary>
public class _11000030 : NpcScript {
    internal _11000030(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000178$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0831180407000180$ 
                // - Bullies are the worst. How can anyone pick on someone weaker than themselves?
                return true;
            default:
                return true;
        }
    }
}
