using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000839: Pochi
/// </summary>
public class _11000839 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003069$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003072$
                // - Do you know who $npcName:11000614[gender:0]$ is? He's a friend of mine in $map:03000135$.
                return 30;
            case (30, 1):
                // $script:0831180407003073$
                // - We first met in Katramus. The Lumina Liberation Army sprung us while we were being transferred to another prison, and we joined up together. 
                return 30;
            case (30, 2):
                // $script:0831180407003074$
                // - We promised that we'd stick together like we did during our time in prison. That was the most difficult time of our lives.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
