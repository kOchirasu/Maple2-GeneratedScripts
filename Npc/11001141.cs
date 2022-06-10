using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001141: Melvo
/// </summary>
public class _11001141 : NpcScript {
    internal _11001141(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0914192507003916$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0914192507003919$ 
                // - Hello, and welcome to the Andrea Family estate. As its caretaker I would love to give you a tour, but I'm afraid I have some eggs to collect. 
                return true;
            default:
                return true;
        }
    }
}
