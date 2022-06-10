using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001147: Magic Pot
/// </summary>
public class _11001147 : NpcScript {
    internal _11001147(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0916043407003991$ 
                // - Read $npcName:11001147$.
                return true;
            case 10:
                // $script:0916043407003992$ 
                // - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
                return true;
            case 20:
                // $script:0916043407003993$ 
                // - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
                switch (selection) {
                    // $script:0916043407003994$
                    // - (Start cooking.)
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0916043407003995$ 
                // - (Add the first ingredient.) 
                switch (selection) {
                    // $script:0916043407003996$
                    // - (Add 10 $itemPlural:30000390$.)
                    case 0:
                        Id = 0; // TODO: 41 | 28
                        return false;
                    // $script:0916043407003997$
                    // - (Add 9 $itemPlural:30000390$.)
                    case 1:
                        Id = 0; // TODO: 42 | 28
                        return false;
                    // $script:0916043407003998$
                    // - (Add 8 $itemPlural:30000390$.)
                    case 2:
                        Id = 0; // TODO: 22 | 28
                        return false;
                    // $script:0916043407003999$
                    // - (Add 7 $itemPlural:30000390$.)
                    case 3:
                        Id = 0; // TODO: 44 | 28
                        return false;
                }
                return true;
            case 22:
                // $script:0916043407004000$ 
                // - <font color="#909090">(Add the second ingredient.)</font> 
                switch (selection) {
                    // $script:0916043407004001$
                    // - (Add 10 $itemPlural:30000392$.)
                    case 0:
                        Id = 0; // TODO: 23 | 28
                        return false;
                    // $script:0916043407004002$
                    // - (Add 9 $itemPlural:30000392$.)
                    case 1:
                        Id = 0; // TODO: 52 | 28
                        return false;
                    // $script:0916043407004003$
                    // - (Add 8 $itemPlural:30000392$.)
                    case 2:
                        Id = 0; // TODO: 53 | 28
                        return false;
                    // $script:0916043407004004$
                    // - (Add 7 $itemPlural:30000392$.)
                    case 3:
                        Id = 0; // TODO: 54 | 28
                        return false;
                }
                return true;
            case 23:
                // $script:0916043407004005$ 
                // - <font color="#909090">(Add the third ingredient.)</font> 
                switch (selection) {
                    // $script:0916043407004006$
                    // - (Add 10 $itemPlural:30000391$.)
                    case 0:
                        Id = 0; // TODO: 61 | 28
                        return false;
                    // $script:0916043407004007$
                    // - (Add 9 $itemPlural:30000391$.)
                    case 1:
                        Id = 0; // TODO: 62 | 28
                        return false;
                    // $script:0916043407004008$
                    // - (Add 8 $itemPlural:30000391$.)
                    case 2:
                        Id = 0; // TODO: 63 | 28
                        return false;
                    // $script:0916043407004009$
                    // - (Add 7 $itemPlural:30000391$.)
                    case 3:
                        Id = 0; // TODO: 24 | 28
                        return false;
                }
                return true;
            case 24:
                // $script:0916043407004010$ 
                // - <font color="#909090">(Add the fourth ingredient.)</font> 
                switch (selection) {
                    // $script:0916043407004011$
                    // - (Add 10 $itemPlural:30000393$.)
                    case 0:
                        Id = 0; // TODO: 71 | 28
                        return false;
                    // $script:0916043407004012$
                    // - (Add 9 $itemPlural:30000393$.)
                    case 1:
                        Id = 0; // TODO: 25 | 28
                        return false;
                    // $script:0916043407004013$
                    // - (Add 8 $itemPlural:30000393$.)
                    case 2:
                        Id = 0; // TODO: 73 | 28
                        return false;
                    // $script:0916043407004014$
                    // - (Add 7 $itemPlural:30000393$.)
                    case 3:
                        Id = 0; // TODO: 74 | 28
                        return false;
                }
                return true;
            case 25:
                // $script:0916043407004015$ 
                // - <font color="#909090">(Continue cooking the dish.)</font>
                switch (selection) {
                    // $script:0916043407004016$
                    // - (Cook over high heat for 5 minutes.)
                    case 0:
                        Id = 35;
                        return false;
                    // $script:0916043407004017$
                    // - (Cook over high heat for 3 minutes.)
                    case 1:
                        Id = 35;
                        return false;
                    // $script:0916043407004018$
                    // - (Cook over low heat for 5 minutes.)
                    case 2:
                        Id = 0; // TODO: 26 | 27
                        return false;
                    // $script:0916043407004019$
                    // - (Cook over low heat for 3 minutes.)
                    case 3:
                        Id = 35;
                        return false;
                }
                return true;
            case 26:
                // $script:0916043407004020$ functionID=1 
                // - <font color="#909090">(The syrupy candy crystallizes into a $item:30000395$ with a pop. 
                //   Quickly, remove the candy from the $npcName:11001147$!)</font>
                return true;
            case 27:
                // $script:0916061207004048$ 
                // - <font color="#909090">(The candy syrup looks ready to collect, but all too late you realize your bag is full. The mixture inside the pot begins to boil, before inexplicably exploding into its original components. You collect the ingredients and place them in your bag.)</font>
                return true;
            case 28:
                // $script:1027175907004302$ 
                // - <font color="#909090">(You don't have enough ingredients.)</font>
                return true;
            case 30:
                // $script:1027182707004383$ 
                // - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
                return true;
            case 35:
                // $script:0916043407004041$ 
                // - <font color="#909090">(The $npcName:11001147$ spits out the ingredients with an angry hiss. <i>Did you make a mistake? You'd better read the $npcName:11001146$ again.</i>)
                return true;
            case 41:
                // $script:1027181907004303$ 
                // - <font color="#909090">(Add the second ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004304$
                    // - (Add 10 $itemPlural:30000392$.)
                    case 0:
                        Id = 0; // TODO: 51 | 28
                        return false;
                    // $script:1027181907004305$
                    // - (Add 9 $itemPlural:30000392$.)
                    case 1:
                        Id = 0; // TODO: 52 | 28
                        return false;
                    // $script:1027181907004306$
                    // - (Add 8 $itemPlural:30000392$.)
                    case 2:
                        Id = 0; // TODO: 53 | 28
                        return false;
                    // $script:1027181907004307$
                    // - (Add 7 $itemPlural:30000392$.)
                    case 3:
                        Id = 0; // TODO: 54 | 28
                        return false;
                }
                return true;
            case 42:
                // $script:1027181907004308$ 
                // - <font color="#909090">(Add the second ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004309$
                    // - (Add 10 $itemPlural:30000392$.)
                    case 0:
                        Id = 0; // TODO: 51 | 28
                        return false;
                    // $script:1027181907004310$
                    // - (Add 9 $itemPlural:30000392$.)
                    case 1:
                        Id = 0; // TODO: 52 | 28
                        return false;
                    // $script:1027181907004311$
                    // - (Add 8 $itemPlural:30000392$.)
                    case 2:
                        Id = 0; // TODO: 53 | 28
                        return false;
                    // $script:1027181907004312$
                    // - (Add 7 $itemPlural:30000392$.)
                    case 3:
                        Id = 0; // TODO: 54 | 28
                        return false;
                }
                return true;
            case 43:
                // $script:1027181907004313$ 
                // - <font color="#909090">(Add the second ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004314$
                    // - (Add 10 $itemPlural:30000392$.)
                    case 0:
                        Id = 0; // TODO: 51 | 28
                        return false;
                    // $script:1027181907004315$
                    // - (Add 9 $itemPlural:30000392$.)
                    case 1:
                        Id = 0; // TODO: 52 | 28
                        return false;
                    // $script:1027181907004316$
                    // - (Add 8 $itemPlural:30000392$.)
                    case 2:
                        Id = 0; // TODO: 53 | 28
                        return false;
                    // $script:1027181907004317$
                    // - (Add 7 $itemPlural:30000392$.)
                    case 3:
                        Id = 0; // TODO: 54 | 28
                        return false;
                }
                return true;
            case 44:
                // $script:1027181907004318$ 
                // - <font color="#909090">(Add the second ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004319$
                    // - (Add 10 $itemPlural:30000392$.)
                    case 0:
                        Id = 0; // TODO: 51 | 28
                        return false;
                    // $script:1027181907004320$
                    // - (Add 9 $itemPlural:30000392$.)
                    case 1:
                        Id = 0; // TODO: 52 | 28
                        return false;
                    // $script:1027181907004321$
                    // - (Add 8 $itemPlural:30000392$.)
                    case 2:
                        Id = 0; // TODO: 53 | 28
                        return false;
                    // $script:1027181907004322$
                    // - (Add 7 $itemPlural:30000392$.)
                    case 3:
                        Id = 0; // TODO: 54 | 28
                        return false;
                }
                return true;
            case 51:
                // $script:1027181907004323$ 
                // - <font color="#909090">(Add the third ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004324$
                    // - (Add 10 $itemPlural:30000391$.)
                    case 0:
                        Id = 0; // TODO: 61 | 28
                        return false;
                    // $script:1027181907004325$
                    // - (Add 9 $itemPlural:30000391$.)
                    case 1:
                        Id = 0; // TODO: 62 | 28
                        return false;
                    // $script:1027181907004326$
                    // - (Add 8 $itemPlural:30000391$.)
                    case 2:
                        Id = 0; // TODO: 63 | 28
                        return false;
                    // $script:1027181907004327$
                    // - (Add 7 $itemPlural:30000391$.)
                    case 3:
                        Id = 0; // TODO: 64 | 28
                        return false;
                }
                return true;
            case 52:
                // $script:1027181907004328$ 
                // - <font color="#909090">(Add the third ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004329$
                    // - (Add 10 $itemPlural:30000391$.)
                    case 0:
                        Id = 0; // TODO: 61 | 28
                        return false;
                    // $script:1027181907004330$
                    // - (Add 9 $itemPlural:30000391$.)
                    case 1:
                        Id = 0; // TODO: 62 | 28
                        return false;
                    // $script:1027181907004331$
                    // - (Add 8 $itemPlural:30000391$.)
                    case 2:
                        Id = 0; // TODO: 63 | 28
                        return false;
                    // $script:1027181907004332$
                    // - (Add 7 $itemPlural:30000391$.)
                    case 3:
                        Id = 0; // TODO: 64 | 28
                        return false;
                }
                return true;
            case 53:
                // $script:1027181907004333$ 
                // - <font color="#909090">(Add the third ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004334$
                    // - (Add 10 $itemPlural:30000391$.)
                    case 0:
                        Id = 0; // TODO: 61 | 28
                        return false;
                    // $script:1027181907004335$
                    // - (Add 9 $itemPlural:30000391$.)
                    case 1:
                        Id = 0; // TODO: 62 | 28
                        return false;
                    // $script:1027181907004336$
                    // - (Add 8 $itemPlural:30000391$.)
                    case 2:
                        Id = 0; // TODO: 63 | 28
                        return false;
                    // $script:1027181907004337$
                    // - (Add 7 $itemPlural:30000391$.)
                    case 3:
                        Id = 0; // TODO: 64 | 28
                        return false;
                }
                return true;
            case 54:
                // $script:1027181907004338$ 
                // - <font color="#909090">(Add the third ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004339$
                    // - (Add 10 $itemPlural:30000391$.)
                    case 0:
                        Id = 0; // TODO: 61 | 28
                        return false;
                    // $script:1027181907004340$
                    // - (Add 9 $itemPlural:30000391$.)
                    case 1:
                        Id = 0; // TODO: 62 | 28
                        return false;
                    // $script:1027181907004341$
                    // - (Add 8 $itemPlural:30000391$.)
                    case 2:
                        Id = 0; // TODO: 63 | 28
                        return false;
                    // $script:1027181907004342$
                    // - (Add 7 $itemPlural:30000391$.)
                    case 3:
                        Id = 0; // TODO: 64 | 28
                        return false;
                }
                return true;
            case 61:
                // $script:1027181907004343$ 
                // - <font color="#909090">(Add the fourth ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004344$
                    // - (Add 10 $itemPlural:30000393$.)
                    case 0:
                        Id = 0; // TODO: 71 | 28
                        return false;
                    // $script:1027181907004345$
                    // - (Add 9 $itemPlural:30000393$.)
                    case 1:
                        Id = 0; // TODO: 72 | 28
                        return false;
                    // $script:1027181907004346$
                    // - (Add 8 $itemPlural:30000393$.)
                    case 2:
                        Id = 0; // TODO: 73 | 28
                        return false;
                    // $script:1027181907004347$
                    // - (Add 7 $itemPlural:30000393$.)
                    case 3:
                        Id = 0; // TODO: 74 | 28
                        return false;
                }
                return true;
            case 62:
                // $script:1027181907004348$ 
                // - <font color="#909090">(Add the fourth ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004349$
                    // - (Add 10 $itemPlural:30000393$.)
                    case 0:
                        Id = 0; // TODO: 71 | 28
                        return false;
                    // $script:1027181907004350$
                    // - (Add 9 $itemPlural:30000393$.)
                    case 1:
                        Id = 0; // TODO: 72 | 28
                        return false;
                    // $script:1027181907004351$
                    // - (Add 8 $itemPlural:30000393$.)
                    case 2:
                        Id = 0; // TODO: 73 | 28
                        return false;
                    // $script:1027181907004352$
                    // - (Add 7 $itemPlural:30000393$.)
                    case 3:
                        Id = 0; // TODO: 74 | 28
                        return false;
                }
                return true;
            case 63:
                // $script:1027181907004353$ 
                // - <font color="#909090">(Add the fourth ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004354$
                    // - (Add 10 $itemPlural:30000393$.)
                    case 0:
                        Id = 0; // TODO: 71 | 28
                        return false;
                    // $script:1027181907004355$
                    // - (Add 9 $itemPlural:30000393$.)
                    case 1:
                        Id = 0; // TODO: 72 | 28
                        return false;
                    // $script:1027181907004356$
                    // - (Add 8 $itemPlural:30000393$.)
                    case 2:
                        Id = 0; // TODO: 73 | 28
                        return false;
                    // $script:1027181907004357$
                    // - (Add 7 $itemPlural:30000393$.)
                    case 3:
                        Id = 0; // TODO: 74 | 28
                        return false;
                }
                return true;
            case 64:
                // $script:1027181907004358$ 
                // - <font color="#909090">(Add the fourth ingredient.)</font> 
                switch (selection) {
                    // $script:1027181907004359$
                    // - (Add 10 $itemPlural:30000393$.)
                    case 0:
                        Id = 0; // TODO: 71 | 28
                        return false;
                    // $script:1027181907004360$
                    // - (Add 9 $itemPlural:30000393$.)
                    case 1:
                        Id = 0; // TODO: 72 | 28
                        return false;
                    // $script:1027181907004361$
                    // - (Add 8 $itemPlural:30000393$.)
                    case 2:
                        Id = 0; // TODO: 73 | 28
                        return false;
                    // $script:1027181907004362$
                    // - (Add 7 $itemPlural:30000393$.)
                    case 3:
                        Id = 0; // TODO: 74 | 28
                        return false;
                }
                return true;
            case 71:
                // $script:1027181907004363$ 
                // - <font color="#909090">(Continue cooking the dish.)</font>
                switch (selection) {
                    // $script:1027181907004364$
                    // - (Cook over high heat for 5 minutes.)
                    case 0:
                        Id = 35;
                        return false;
                    // $script:1027181907004365$
                    // - (Cook over high heat for 3 minutes.)
                    case 1:
                        Id = 35;
                        return false;
                    // $script:1027181907004366$
                    // - (Cook over low heat for 5 minutes.)
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1027181907004367$
                    // - (Cook over low heat for 3 minutes.)
                    case 3:
                        Id = 35;
                        return false;
                }
                return true;
            case 72:
                // $script:1027181907004368$ 
                // - <font color="#909090">(Continue cooking the dish.)</font>
                switch (selection) {
                    // $script:1027181907004369$
                    // - (Cook over high heat for 5 minutes.)
                    case 0:
                        Id = 35;
                        return false;
                    // $script:1027181907004370$
                    // - (Cook over high heat for 3 minutes.)
                    case 1:
                        Id = 35;
                        return false;
                    // $script:1027181907004371$
                    // - (Cook over low heat for 5 minutes.)
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1027181907004372$
                    // - (Cook over low heat for 3 minutes.)
                    case 3:
                        Id = 35;
                        return false;
                }
                return true;
            case 73:
                // $script:1027181907004373$ 
                // - <font color="#909090">(Continue cooking the dish.)</font>
                switch (selection) {
                    // $script:1027181907004374$
                    // - (Cook over high heat for 5 minutes.)
                    case 0:
                        Id = 35;
                        return false;
                    // $script:1027181907004375$
                    // - (Cook over high heat for 3 minutes.)
                    case 1:
                        Id = 35;
                        return false;
                    // $script:1027181907004376$
                    // - (Cook over low heat for 5 minutes.)
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1027181907004377$
                    // - (Cook over low heat for 3 minutes.)
                    case 3:
                        Id = 35;
                        return false;
                }
                return true;
            case 74:
                // $script:1027181907004378$ 
                // - <font color="#909090">(Continue cooking the dish.)</font>
                switch (selection) {
                    // $script:1027181907004379$
                    // - (Cook over high heat for 5 minutes.)
                    case 0:
                        Id = 35;
                        return false;
                    // $script:1027181907004380$
                    // - (Cook over high heat for 3 minutes.)
                    case 1:
                        Id = 35;
                        return false;
                    // $script:1027181907004381$
                    // - (Cook over low heat for 5 minutes.)
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1027181907004382$
                    // - (Cook over low heat for 3 minutes.)
                    case 3:
                        Id = 35;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
