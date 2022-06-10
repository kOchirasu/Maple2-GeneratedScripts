using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003587: 
/// </summary>
public class _11003587 : NpcScript {
    internal _11003587(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102131310001928$ 
                // - Happy birthday!
                return true;
            case 10:
                // $script:1102131310001929$ 
                // - Come see me on the month of your birthday—that is, the anniversy of the month you created your account. You'll get a special birthday blessing and gift!
                return true;
            default:
                return true;
        }
    }
}
