using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003127: Rowen
/// </summary>
public class _11003127 : NpcScript {
    internal _11003127(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0131174207007912$ 
                // - The Lumiknights are watching you. 
                return true;
            case 10:
                // $script:0207122607007946$ 
                // - I don't know how big the Lumiknights' organization is, but our numbers in Tria are just a fraction of the whole. 
                return true;
            default:
                return true;
        }
    }
}
