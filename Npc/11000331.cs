using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000331: Brandon
/// </summary>
public class _11000331 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001339$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001341$
                // - Hm... Have you ever felt like you're being watched? You get this itchy feeling on the back of your neck when that happens. I've been feeling it a lot lately. Why do you think that is?
                return -1;
            case (30, 0):
                // $script:0831180407001342$
                // - Excuse me, have you seen a girl around here who looks like me? She has blond hair and blue eyes, just like I do. I don't remember what she was wearing, though.
                return 30;
            case (30, 1):
                // $script:0831180407001343$
                // - She's my sister. She went to do her hair and never came back. Does it take women a long time to do their hair? Huh... maybe she was getting it dyed.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
