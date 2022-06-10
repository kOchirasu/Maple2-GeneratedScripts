using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001146: Recipe Note
/// </summary>
public class _11001146 : NpcScript {
    internal _11001146(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;21;23
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0916043407003980$ 
                // - Read $npcName:11001146$.
                return true;
            case 10:
                // $script:0916043407003981$ 
                // - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
                //   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
                //   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
                // $script:0916043407003982$ 
                // - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
                //   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
                //   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
                return true;
            case 20:
                // $script:0916043407003983$ 
                // - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
                //   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
                //   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
                // $script:0916043407003984$ 
                // - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
                //   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
                //   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
                switch (selection) {
                    // $script:0916043407003985$
                    // - (Read it again.)
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0916043407003986$
                    // - (Read the back side.)
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:0916043407003987$ 
                // - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
                //   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
                //   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
                // $script:0916043407003988$ 
                // - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
                //   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
                //   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
                switch (selection) {
                    // $script:0916060407004042$
                    // - (Read it again.)
                    case 0:
                        Id = 23;
                        return false;
                    // $script:0916060407004043$
                    // - (Read the back side.)
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 22:
                // $script:0916043407003989$ 
                // - <u><font color="#FA5656">Cooking the $item:30000395$</font></u>
                //   <b>1.</b> While stirring, gradually add the following ingredients to the <i>$npcName:11001147$</i>:
                //   <font color="#ffd200">8 $itemPlural:30000390$</font>, <font color="#ffd200">10 $itemPlural:30000392$</font>, <font color="#ffd200"> 7 $itemPlural:30000391$</font>, and <font color="#ffd200">9 $itemPlural:30000393$</font>
                // $script:0916043407003990$ 
                // - <b>2.</b> Cook over low heat for 5 minutes, stirring until uniform in consistency.
                //   <b>3.</b> Pour and let harden
                //   <font size="20" color="#FC0404">      *Note: $npcName:11001147$ is finicky. Remove cooked candy immediately.</font>
                return true;
            case 23:
                // $script:0916060407004044$ 
                // - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
                //   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
                //   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
                // $script:0916060407004045$ 
                // - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
                //   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
                //   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
                switch (selection) {
                    // $script:0916060407004046$
                    // - (Read it again.)
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0916060407004047$
                    // - (Read the back side.)
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
