using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000484: Luccachi
/// </summary>
public class _11000484 : NpcScript {
    internal _11000484(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002126$ 
                // - What's wrong? 
                return true;
            case 30:
                // $script:0831180407002128$ 
                // - Yeesh, I don't know if they'll have room for me. I've been out all day. I really need to put my feet up.  
                return true;
            default:
                return true;
        }
    }
}
