using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004435: Condor
/// </summary>
public class _11004435 : NpcScript {
    internal _11004435(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011974$ 
                // - Back in my day, we knew a thing or two about duty! 
                return true;
            case 10:
                // $script:1213154907011975$ 
                // - Don't look so glum, Cadet. We're in a new land full of new and exciting things to eat! 
                return true;
            default:
                return true;
        }
    }
}
