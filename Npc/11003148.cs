using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003148: Einos
/// </summary>
public class _11003148 : NpcScript {
    internal _11003148(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0324141007008127$ 
                // - Did you remember your books? 
                return true;
            case 10:
                // $script:0324141007008128$ 
                // - Of course you didn't. I don't know what I expected. 
                return true;
            default:
                return true;
        }
    }
}
