using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001097: Triz
/// </summary>
public class _11001097 : NpcScript {
    internal _11001097(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003688$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407003691$ 
                // - If I had to pick my most popular invention, it would be NSD 3200. It's a device that dismantles equipment and extracts onyx from it.
                // $script:0831180407003692$ 
                // - People think the blacksmiths of the Nerman Forge came up with it, but I was brought in to design it for them. I was compensated for my services, of course, but if I knew it'd become so popular I would've asked for more royalties!
                return true;
            default:
                return true;
        }
    }
}
