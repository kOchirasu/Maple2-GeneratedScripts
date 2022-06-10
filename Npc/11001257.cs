using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001257: Moren
/// </summary>
public class _11001257 : NpcScript {
    internal _11001257(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203001410001288$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:1203001410001290$ 
                // - You said you wanted me to send you where $npcName:11001229[gender:0]$ went, right? Well, that would be an inn on Victoria Island, in the city of Tria. Would you like to go there now?
                return true;
            case 30:
                // $script:1203001410001294$ 
                // - Ever wish you could get somewhere instantaneously? What would you say if I told you I could use a bit of rune magic to send you wherever you want in the blink of an eye?
                switch (selection) {
                    // $script:1203001410001295$
                    // - Please teleport me!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1203001410001296$ 
                // - You won't believe it 'til it happens! Oh. Um... just a moment. Uh, it seems I don't have enough rune energy on-hand for the teleportation spell.
                // $script:1203001410001297$ 
                // - Hmm. You still have things left to do here anyway, don't you? Maybe you should take care of those. I'm not stalling!
                return true;
            default:
                return true;
        }
    }
}
