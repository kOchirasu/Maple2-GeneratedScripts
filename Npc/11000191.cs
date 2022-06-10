using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000191: Mrs. Hofmann
/// </summary>
public class _11000191 : NpcScript {
    internal _11000191(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000858$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407000861$ 
                // - I think my husband should've married his job instead of me. He's never home. 
                return true;
            case 30:
                // $script:0831180407000862$ 
                // - I used to love the aroma of herbs that followed my husband, but that was before we married. He's so obsessed with them now that he never has time to help around the house. 
                // $script:0831180407000863$ 
                // - Sometimes I wonder... I wonder if I should take the kids to $map:02000002$ for a fresh start. There's more to being a good husband than just putting food on the table.  
                return true;
            default:
                return true;
        }
    }
}
