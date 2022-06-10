using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004231: Cheri Ring
/// </summary>
public class _11004231 : NpcScript {
    internal _11004231(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809134507010879$ 
                // - Hello, $MyPCName$!
                return true;
            case 30:
                // $script:0808172007010838$ 
                // - You must be here about this fancy chest, yes? It's enchanted to provide you with the materials you need to upgrade your gemstones.
                // $script:0808172007010839$ 
                // - Go ahead and give it a try. You'll need the proper reagents to open it, of course.
                switch (selection) {
                    // $script:0808172007010840$
                    // - What reagents do I need?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0808172007010841$
                    // - I'm curious about the science behind this.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0808172007010842$ 
                // - You'll want some $itemPlural:30001187$, which you can get by hunting monsters. That's the raw material that you will turn into gemstones.
                // $script:0808172007010843$ 
                // - To trigger the reaction, just use some $item:30001188$, and viola!
                switch (selection) {
                    // $script:0808172007010844$
                    // - How do I get those?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0808172007010845$ 
                // - Fortunately for you, I just so happen to sell them! I should warn you, though, that my supply is pretty limited. It's not easy to make, you know.
                return true;
            case 33:
                // $script:0808172007010846$ 
                // - $npc:11000601[gender:1]$ discovered this chest while taking inventory of the royal reliquary. We think it was a gift to the empress from a faraway place. Anyway, it seems to turn the energy of monsters into something useful.
                // $script:0808172007010847$ 
                // - The $npc:11004215$, as we've taken to calling it, can convert all kinds of energy. As soon as she found it, $npcName:11000601[gender:1]$ set herself to researching the device.
                // $script:0808172007010848$ 
                // - To her surprise, the chest was even able to take the $item:30001187$ taken from monsters and turn it into gem dust. We agreed that it would be in everyone's best interest to make this device freely available to adventurer's like you!
                // $script:0809134507010880$ 
                // - Now, you will need $item:30001188$ to stabilize the process. It's simple physics, as I'm sure you know.
                switch (selection) {
                    // $script:0809134507010881$
                    // - What materials do I need?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 60:
                // $script:0911145207011163$ 
                // - The empress has declared that all experienced adventurers shall have access to this enchanted chest here! Not you, though. I'm afraid you're not quite experienced enough. Would you be so kind as to come back when you're level 50?
                return true;
            default:
                return true;
        }
    }
}
