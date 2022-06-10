using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004147: Ralph
/// </summary>
public class _11004147 : NpcScript {
    internal _11004147(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010565$ 
                // - What do you want? 
                return true;
            case 10:
                // $script:0806025707010566$ 
                // - This place is gonna make me rich! I've just gotta figure out how, first... 
                return true;
            default:
                return true;
        }
    }
}
