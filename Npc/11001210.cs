using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001210: 
/// </summary>
public class _11001210 : NpcScript {
    internal _11001210(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1022122107004244$ 
                // - Life is a cycle.
                return true;
            case 30:
                // $script:1022122107004247$ 
                // - There is a <font color="#ffd200">lifeforce</font> all around us. It's in the leaves and the breeze, the water, and the very earth we tread. I've always wondered from where life originates.
                switch (selection) {
                    // $script:1022122107004248$
                    // - Any thoughts on the topic?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1022122107004249$ 
                // - Well, I don't know about a direct source... But there is clearly a natural order to things. A cycle of life.
                switch (selection) {
                    // $script:1022122107004250$
                    // - What do you mean?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1022122107004251$ 
                // - Flowers, monsters, and people alike. Everything is born from nature, and returns to nature when its time is at an end. There is an endless cycle of life that keeps this world balanced.
                return true;
            case 40:
                // $script:1023213007004272$ 
                // - Oh, you've brought me more $item:30000419$. 
                //   Allow me to extract the $item:30000420$ that lies within. Give me a moment.
                switch (selection) {
                    // $script:1023213007004273$
                    // - (Hand over the $item:30000419$.)
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1023213007004276$ 
                // - Primordial Nature, Mother of Earth, I beseech thee! Make me your conduit and return this tainted spirit to the source of all life! <i>Aniriel zu spiritalis... Ritana vitalitas!</i>
                // $script:1023213007004277$ functionID=1 
                // - It worked! Here, this $item:30000420$ was inside it. I hope you'll use it for good.
                return true;
            case 50:
                // $script:1023213007004274$ 
                // - Give me the $item:30000419$. I'm not sure if this will work, but it's worth a shot.
                switch (selection) {
                    // $script:1023213007004275$
                    // - (Hand over the $item:30000419$.)
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 51:
                // $script:1023213007004278$ 
                // - Primordial Nature, Mother of Earth, I beseech thee! Make me your conduit and return this tainted spirit to the source of all life! <i>Aniriel zu spiritalis... Ritana vitalitas!</i>
                switch (selection) {
                    // $script:1023223707004280$
                    // - (You wait for Lileaf to finish chanting.)
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1023213007004279$ functionID=1 
                // - It worked! Here, this $item:30000420$ was inside it. I hope you'll use it for good.
                return true;
            default:
                return true;
        }
    }
}
