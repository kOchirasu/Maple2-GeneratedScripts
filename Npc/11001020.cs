using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001020: Clarke
/// </summary>
public class _11001020 : NpcScript {
    internal _11001020(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003467$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0908154107003709$ 
                // - I can feel time being restored to order. This means there isn't much of it left for us to spend together. 
                return true;
            default:
                return true;
        }
    }
}
