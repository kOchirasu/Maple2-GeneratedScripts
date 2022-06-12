using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001210: 
/// </summary>
public class _11001210 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 30;40;50
        // (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (40, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (50, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1022122107004244$ 
                // - Life is a cycle.
                return default;
            case 30:
                // $script:1022122107004247$ 
                // - There is a <font color="#ffd200">lifeforce</font> all around us. It's in the leaves and the breeze, the water, and the very earth we tread. I've always wondered from where life originates.
                switch (selection) {
                    // $script:1022122107004248$
                    // - Any thoughts on the topic?
                    case 0:
                        return (31, NpcTalkButton.SelectableDistractor);
                }
                return default;
            case 31:
                // $script:1022122107004249$ 
                // - Well, I don't know about a direct source... But there is clearly a natural order to things. A cycle of life.
                switch (selection) {
                    // $script:1022122107004250$
                    // - What do you mean?
                    case 0:
                        return (32, NpcTalkButton.Close);
                }
                return default;
            case 32:
                // $script:1022122107004251$ 
                // - Flowers, monsters, and people alike. Everything is born from nature, and returns to nature when its time is at an end. There is an endless cycle of life that keeps this world balanced.
                return default;
            case 40:
                // $script:1023213007004272$ 
                // - Oh, you've brought me more $item:30000419$. 
                //   Allow me to extract the $item:30000420$ that lies within. Give me a moment.
                switch (selection) {
                    // $script:1023213007004273$
                    // - (Hand over the $item:30000419$.)
                    case 0:
                        return (41, NpcTalkButton.Next);
                }
                return default;
            case 41:
                switch (Index++) {
                    case 0:
                        // $script:1023213007004276$ 
                        // - Primordial Nature, Mother of Earth, I beseech thee! Make me your conduit and return this tainted spirit to the source of all life! <i>Aniriel zu spiritalis... Ritana vitalitas!</i>
                        return (41, NpcTalkButton.Close);
                    case 1:
                        // $script:1023213007004277$ functionID=1 
                        // - It worked! Here, this $item:30000420$ was inside it. I hope you'll use it for good.
                        return default;
                }
                break;
            case 50:
                // $script:1023213007004274$ 
                // - Give me the $item:30000419$. I'm not sure if this will work, but it's worth a shot.
                switch (selection) {
                    // $script:1023213007004275$
                    // - (Hand over the $item:30000419$.)
                    case 0:
                        return (41, NpcTalkButton.Next);
                }
                return default;
            case 51:
                // $script:1023213007004278$ 
                // - Primordial Nature, Mother of Earth, I beseech thee! Make me your conduit and return this tainted spirit to the source of all life! <i>Aniriel zu spiritalis... Ritana vitalitas!</i>
                switch (selection) {
                    // $script:1023223707004280$
                    // - (You wait for Lileaf to finish chanting.)
                    case 0:
                        return (52, NpcTalkButton.Close);
                }
                return default;
            case 52:
                // $script:1023213007004279$ functionID=1 
                // - It worked! Here, this $item:30000420$ was inside it. I hope you'll use it for good.
                return default;
        }
        
        return default;
    }
}
