using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001193: Illuna
/// </summary>
public class _11001193 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004180$
    // - I wish I could find a story my colleague $npcName:11001191[gender:1]$ would be excited to cover.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004183$
                // - Hehehe! This is so much fun! <font color="#C66455" size="22">Pfft... Are you kidding me? This is awful.</font> 
                //   No, no. Don't say that.
                //   <font color="#909090">(...Is she arguing with herself?)</font>
                return 30;
            case (30, 1):
                // $script:1016210507004212$
                // - ...?! Ahh! How long have you been standing there? You didn't hear what I said, did you?
                switch (selection) {
                    // $script:1016210507004213$
                    // - Uhh... Were you just talking to yourself?
                    case 0:
                        return 31;
                    // $script:1016210507004214$
                    // - I didn't hear a thing.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004186$
                // - W-what? I'm not crazy, you're crazy! <font color="#C66455" size="22">I didn't say anything, got it?</font>
                //   <font color="#909090">(After an awkward silence, Illuna sighs in resignation.)</font>
                return -1;
            case (32, 0):
                // $script:1016202007004187$
                // - Hah... Hahaha! 
                //   <font color="#C66455" size="22">Good, good.</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
