using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000200: Neal
/// </summary>
public class _11000200 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000869$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000872$
                // - $npcName:11000202[gender:0]$ is really dumb. Did you see him standing there? He's punishing himself! 
                return -1;
            case (40, 0):
                // $script:0831180407000873$
                // - $npcName:11000201[gender:0]$ is my friend from $map:02000023$. He's an elf. Isn't that awesome? 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
