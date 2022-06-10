using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004264: Khalifa Building
/// </summary>
public class _11004264 : NpcScript {
    internal _11004264(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011188$ 
                // - <font color="#909090">(This is the directory to the $npcName:11004264$.)</font>
                //   <i>Welcome to $npcName:11004264$, the pride of $map:02010002$! As the biggest multiplex shopping center on Karkar Island, we have what you're looking for!</i>
                return true;
            case 10:
                // $script:0911203207011189$ 
                // - <font color="#909090">(This is the directory to the $npcName:11004264$.)</font>
                //   <i>Welcome to $npcName:11004264$, the pride of $map:02010002$! As the biggest multiplex shopping center on Karkar Island, we have what you're looking for!</i>
                // $script:0911203207011190$ 
                // - <font color="#ffd200">1F</font>
                //   <i>Cosmetics, Accessories, General Merchandise
                //   Offering a truly premium shopping experience, with direct imports from all over Maple World.</i>
                // $script:0911203207011191$ 
                // - <font color="#ffd200">2F</font>
                //   <i>Fashion, Shoes, Handbags
                //   The hottest brands from all over the world in one place.</i>
                // $script:0911203207011192$ 
                // - <font color="#ffd200">3F</font>
                //   <i>Youth Fashion
                //   The latest trends, straight from the streets.</i>
                // $script:0911203207011193$ 
                // - <font color="#ffd200">4F</font>
                //   <i>Sports
                //   Sportswear and supplies to help you and your family stay in shape.</i>
                // $script:0911203207011194$ 
                // - <font color="#ffd200">5F</font>
                //   <i>Men's Fashion
                //   A careful curation of the best men's brands in fashion, tech, and accessories.</i>
                // $script:0911203207011195$ 
                // - <font color="#ffd200">6F</font>
                //   <i>Kids, Food Court
                //   From toys to fashion, everything a kid could want. Don't forget to check out the premium restaurants, perfect for any palette.</i>
                return true;
            default:
                return true;
        }
    }
}
