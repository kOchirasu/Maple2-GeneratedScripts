using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003829: Balrog
/// </summary>
public class _11003829 : NpcScript {
    internal _11003829(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0115140307009755$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0115140307009756$ 
                // - Those slimeballs... 
                return true;
            default:
                return true;
        }
    }
}
