using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004217: Jenna
/// </summary>
public class _11004217 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0806222707010773$
    // - Do you have business with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010774$
                // - Haha, let's get this party started! Pew pew! That's the sound of me blowing everyone away with the power of my cannon!
                return -1;
            case (20, 0):
                // $script:0806222707010775$
                // - If you want to be happy, there's one rule to live by: figure out what you wanna do, and do it! In my case, that's listening my cannon purr as it pumps out hundreds of rounds a minute.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
