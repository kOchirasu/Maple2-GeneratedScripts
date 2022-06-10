using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004222: Cheriffe
/// </summary>
public class _11004222 : NpcScript {
    internal _11004222(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010791$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0806222707010792$ 
                // - In my line of work, discretion and poise are vital. That makes this dapper fellow a very hot commodity...
                return true;
            default:
                return true;
        }
    }
}
