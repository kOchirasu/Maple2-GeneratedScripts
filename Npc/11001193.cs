using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001193: Illuna
/// </summary>
public class _11001193 : NpcScript {
    internal _11001193(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004180$ 
                // - I wish I could find a story my colleague $npcName:11001191[gender:1]$ would be excited to cover. 
                return true;
            case 30:
                // $script:1016202007004183$ 
                // - Hehehe! This is so much fun! <font color="#C66455" size="22">Pfft... Are you kidding me? This is awful.</font> 
No, no. Don't say that.
<font color="#909090">(...Is she arguing with herself?)</font> 
                // $script:1016210507004212$ 
                // - ...?! Ahh! How long have you been standing there? You didn't hear what I said, did you? 
                switch (selection) {
                    // $script:1016210507004213$
                    // - Uhh... Were you just talking to yourself?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1016210507004214$
                    // - I didn't hear a thing.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004186$ 
                // - W-what? I'm not crazy, you're crazy! <font color="#C66455" size="22">I didn't say anything, got it?</font>
<font color="#909090">(After an awkward silence, Illuna sighs in resignation.)</font> 
                return true;
            case 32:
                // $script:1016202007004187$ 
                // - Hah... Hahaha! 
<font color="#C66455" size="22">Good, good.</font> 
                return true;
            default:
                return true;
        }
    }
}
