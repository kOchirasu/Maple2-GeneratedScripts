using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004331: Orde
/// </summary>
public class _11004331 : NpcScript {
    internal _11004331(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011633$ 
                // - Those four... It can't be...
                return true;
            case 20:
                // $script:1010140307011551$ 
                // - Those four... It can't be...
                return true;
            case 10:
                // $script:1102172107011634$ 
                // - Children of the dragon... here? Am I dreaming?
                return true;
            case 30:
                // $script:1010140307011552$ 
                // - Children of the dragon... here? Am I dreaming?
                switch (selection) {
                    // $script:1010140307011553$
                    // - (Tap her gently on the shoulder.)
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011554$ 
                // - Ahh! Don't sneak up on a girl like that!
                // $script:1010140307011555$ 
                // - Oh, it's you. I didn't expect to run into you here.
                // $script:1010140307011556$ 
                // - I'm busy right now. Can we talk later?
                switch (selection) {
                    // $script:1010140307011557$
                    // - What are you doing?
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011558$ 
                // - It's top-secret!
                // $script:1010140307011559$ 
                // - Actually, you'll never believe it. Those kids raised by the last dragon master? They're <b>here</b>!
                // $script:1010140307011560$ 
                // - I heard the rumors. That's the only reason I was willing to come schlep all the way here with $npcName:11004332[gender:1]$. But it turns out they were true!
                // $script:1010140307011561$ 
                // - See that girl with the blonde hair, way over there? I can smell her dragon juju from here. Unless I'm imagining things...
                // $script:1010140307011562$ 
                // - What I would give for an interview with them! Just to hear them talk about the lumarigons...
                switch (selection) {
                    // $script:0111232407012697$
                    // - Same old Orde.
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0111232407012698$ 
                // - Hey, you know them don't you? Do you think you could introduce me? Please? Hey, where are you going?!
                return true;
            default:
                return true;
        }
    }
}
